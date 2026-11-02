"""Career Counselor

Task: Switch from teaching to UX design.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'career_counselor'
TITLE = 'Career Counselor'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Switch from teaching to UX design.'

# (key, role, instruction)
AGENTS = [
    ('skills_mapper', 'Skills Mapper', 'Map skills.'),
    ('market_scout', 'Market Scout', 'Describe market.'),
    ('gap_analyzer', 'Gap Analyzer', 'Find gaps.'),
    ('learning_path_designer', 'Learning Path Designer', 'Design path.'),
    ('networking_coach', 'Networking Coach', 'Networking plan.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
