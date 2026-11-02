"""Language Tutor

Task: Practice ordering food in Spanish.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'language_tutor'
TITLE = 'Language Tutor'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Practice ordering food in Spanish.'

# (key, role, instruction)
AGENTS = [
    ('level_assessor', 'Level Assessor', 'Assess level.'),
    ('dialogue_generator', 'Dialogue Generator', 'Write dialogue.'),
    ('grammar_coach', 'Grammar Coach', 'Explain grammar.'),
    ('pronunciation_tips_agent', 'Pronunciation Tips Agent', 'Give tips.'),
    ('progress_reporter', 'Progress Reporter', 'Track progress.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
