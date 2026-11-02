"""Library Assistant

Task: Recommend books on urban gardening.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'library_assistant'
TITLE = 'Library Assistant'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Recommend books on urban gardening.'

# (key, role, instruction)
AGENTS = [
    ('interest_profiler', 'Interest Profiler', 'Understand interests.'),
    ('catalog_searcher', 'Catalog Searcher', 'Find candidates.'),
    ('reading_level_matcher', 'Reading Level Matcher', 'Match level.'),
    ('recommender', 'Recommender', 'Recommend.'),
    ('reservation_agent', 'Reservation Agent', 'Reserve.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
