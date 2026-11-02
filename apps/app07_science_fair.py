"""Science Fair Mentor

Task: Help a student design a plant-growth experiment.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'science_fair'
TITLE = 'Science Fair Mentor'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Help a student design a plant-growth experiment.'

# (key, role, instruction)
AGENTS = [
    ('question_refiner', 'Question Refiner', 'Refine question.'),
    ('hypothesis_coach', 'Hypothesis Coach', 'Write hypothesis.'),
    ('method_designer', 'Method Designer', 'Design method.'),
    ('safety_checker', 'Safety Checker', 'Check safety.'),
    ('presentation_coach', 'Presentation Coach', 'Plan presentation.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
