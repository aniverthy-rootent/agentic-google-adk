"""Study Abroad Advisor

Task: Plan a semester in Sweden for an engineering student.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'study_abroad'
TITLE = 'Study Abroad Advisor'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Plan a semester in Sweden for an engineering student.'

# (key, role, instruction)
AGENTS = [
    ('program_matcher', 'Program Matcher', 'Match programs.'),
    ('visa_advisor', 'Visa Advisor', 'Visa overview.'),
    ('housing_agent', 'Housing Agent', 'Housing options.'),
    ('budget_planner', 'Budget Planner', 'Budget.'),
    ('checklist_agent', 'Checklist Agent', 'Pre-departure checklist.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
