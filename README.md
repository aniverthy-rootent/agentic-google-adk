# agentic-google-adk

**11 multi-agent applications built with Google Agent Development Kit (ADK).**  
Theme: _Education, learning & public-service assistants (Google ADK)_

[Google's Agent Development Kit](https://google.github.io/adk-docs/) (ADK) builds agents from `LlmAgent` plus workflow agents (`SequentialAgent`, `ParallelAgent`, `LoopAgent`). These apps are education and public-service assistants.

## Quick start (no API key needed)

```bash
pip install -r requirements.txt
python run_all.py                       # run all 11 apps
python -m apps.app01_lesson_planner   # run a single app
pytest -q                               # smoke tests for every app
```

Every app runs against a deterministic offline model (`common/offline_llm.py`) so you can watch the orchestration work without credentials.

## How it works

Each role is an `LlmAgent` that saves its answer to session state via `output_key`; downstream instructions reference upstream answers with `{key}` templating. Fan-out apps use `SequentialAgent([planner, ParallelAgent([...]), merger])`. An offline `BaseLlm` replaces Gemini.

## Using a real model

Pass a model string to `build_root(..., model='gemini-2.5-flash')` (set `GOOGLE_API_KEY`), or wrap another provider with `google.adk.models.lite_llm.LiteLlm(model='anthropic/claude-sonnet-5-5')`.

## Applications

| # | Application | Agents | Roles |
|---|---|---|---|
| 1 | Lesson Planner | 5 | Curriculum Mapper, Objective Writer, Activity Designer, Assessment Designer, Differentiation Agent |
| 2 | Language Tutor | 5 | Level Assessor, Dialogue Generator, Grammar Coach, Pronunciation Tips Agent, Progress Reporter |
| 3 | Career Counselor | 5 | Skills Mapper, Market Scout, Gap Analyzer, Learning Path Designer, Networking Coach |
| 4 | City Services Assistant | 5 | Request Classifier, Reporter Agent, Schedule Agent, Status Tracker, Notifier |
| 5 | Library Assistant | 5 | Interest Profiler, Catalog Searcher, Reading Level Matcher, Recommender, Reservation Agent |
| 6 | Disaster Response Coordinator | 5 | Situation Analyst, Shelter Planner, Supply Coordinator, Volunteer Manager, Public Information Officer |
| 7 | Science Fair Mentor | 5 | Question Refiner, Hypothesis Coach, Method Designer, Safety Checker, Presentation Coach |
| 8 | Essay Grader | 5 | Rubric Loader, Content Grader, Structure Grader, Language Grader, Feedback Writer |
| 9 | School-Parent Communications | 5 | Fact Collector, Message Writer, Translator, Accessibility Checker, Distribution Planner |
| 10 | Museum Guide | 5 | Exhibit Researcher, Route Planner, Storyteller, Accessibility Advisor, Q&A Agent |
| 11 | Study Abroad Advisor | 5 | Program Matcher, Visa Advisor, Housing Agent, Budget Planner, Checklist Agent |

Full per-agent instructions are in [AGENTS.md](AGENTS.md).

Each app uses one of two data-flow patterns (see `common/flow.py`):
`sequential` (each agent builds on the previous) or `fanout` (a planner, parallel specialists, then a merger).

## License

MIT
