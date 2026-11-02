"""Museum Guide

Task: Create a 60-minute tour of an impressionism exhibit.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'museum_guide'
TITLE = 'Museum Guide'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Create a 60-minute tour of an impressionism exhibit.'

# (key, role, instruction)
AGENTS = [
    ('exhibit_researcher', 'Exhibit Researcher', 'Research works.'),
    ('route_planner', 'Route Planner', 'Plan route.'),
    ('storyteller', 'Storyteller', 'Narrate.'),
    ('accessibility_advisor', 'Accessibility Advisor', 'Accessibility notes.'),
    ('q_a_agent', 'Q&A Agent', 'Prepare Q&A.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
