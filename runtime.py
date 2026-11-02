"""Google ADK runtime: LlmAgents composed with SequentialAgent / ParallelAgent.

* every role is an LlmAgent with `output_key`, so its answer lands in session state
* downstream agents read upstream answers through ADK instruction templating
  (`{key}` placeholders are filled from session state)
* fan-out apps use SequentialAgent([planner, ParallelAgent([specialists]), merger])
An offline BaseLlm subclass replaces Gemini.
"""
from __future__ import annotations

import asyncio
from typing import AsyncGenerator

from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.models.base_llm import BaseLlm
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.adk.runners import InMemoryRunner
from google.genai import types

from common.flow import FANOUT, dependencies
from common.offline_llm import offline_complete


class OfflineLlm(BaseLlm):
    """ADK model with no network access. Replace with model='gemini-2.5-flash' (or LiteLlm)."""

    model: str = "offline"

    async def generate_content_async(self, llm_request: LlmRequest, stream: bool = False
                                     ) -> AsyncGenerator[LlmResponse, None]:
        instruction = llm_request.config.system_instruction if llm_request.config else ""
        if not isinstance(instruction, str):
            instruction = " ".join(getattr(p, "text", "") or "" for p in getattr(instruction, "parts", []) or [])
        text = offline_complete(instruction, instruction)
        yield LlmResponse(content=types.Content(role="model", parts=[types.Part(text=text)]))


def build_root(agents, task, pattern, model=None):
    model = model or OfflineLlm()
    deps = dependencies(pattern, len(agents))
    llm_agents = []
    for i, (key, role, instr) in enumerate(agents):
        upstream = "".join(f"\n- {agents[j][1]}: {{{agents[j][0]}}}" for j in deps[i])
        instruction = (f"{role}\nYou are the {role} in a multi-agent team. {instr}\n"
                       f"Task: {task}" + (f"\nUpstream results:{upstream}" if upstream else ""))
        llm_agents.append(LlmAgent(name=key, model=model, description=instr,
                                   instruction=instruction, output_key=key))
    n = len(agents)
    if pattern == FANOUT and n >= 4:
        return SequentialAgent(name="team", sub_agents=[
            llm_agents[0], ParallelAgent(name="specialists", sub_agents=llm_agents[1:-1]), llm_agents[-1]])
    return SequentialAgent(name="team", sub_agents=llm_agents)


async def _run(agents, task, pattern):
    runner = InMemoryRunner(agent=build_root(agents, task, pattern), app_name="agentic_adk")
    session = await runner.session_service.create_session(app_name="agentic_adk", user_id="user")
    async for _ in runner.run_async(user_id="user", session_id=session.id,
                                    new_message=types.Content(role="user", parts=[types.Part(text=task)])):
        pass
    session = await runner.session_service.get_session(app_name="agentic_adk", user_id="user", session_id=session.id)
    return {key: str(session.state[key]) for key, _, _ in agents}


def run_app(title, agents, task, pattern="sequential", provider=None) -> dict:
    return asyncio.run(_run(agents, task, pattern))
