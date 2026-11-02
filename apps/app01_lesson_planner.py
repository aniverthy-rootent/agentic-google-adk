"""Lesson Planner

Task: Plan a 45-minute lesson on photosynthesis for grade 7.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'lesson_planner'
TITLE = 'Lesson Planner'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Plan a 45-minute lesson on photosynthesis for grade 7.'

# (key, role, instruction)
AGENTS = [
    ('curriculum_mapper', 'Curriculum Mapper', 'Map standards.'),
    ('objective_writer', 'Objective Writer', 'Write objectives.'),
    ('activity_designer', 'Activity Designer', 'Design activities.'),
    ('assessment_designer', 'Assessment Designer', 'Design assessment.'),
    ('differentiation_agent', 'Differentiation Agent', 'Adapt for learners.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
