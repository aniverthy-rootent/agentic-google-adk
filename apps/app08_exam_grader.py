"""Essay Grader

Task: Grade a 500-word essay on climate policy.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'exam_grader'
TITLE = 'Essay Grader'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Grade a 500-word essay on climate policy.'

# (key, role, instruction)
AGENTS = [
    ('rubric_loader', 'Rubric Loader', 'Define rubric.'),
    ('content_grader', 'Content Grader', 'Grade content.'),
    ('structure_grader', 'Structure Grader', 'Grade structure.'),
    ('language_grader', 'Language Grader', 'Grade language.'),
    ('feedback_writer', 'Feedback Writer', 'Write feedback.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
