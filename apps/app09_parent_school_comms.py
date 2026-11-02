"""School-Parent Communications

Task: Announce a schedule change for sports day.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'parent_school_comms'
TITLE = 'School-Parent Communications'
PATTERN = 'sequential'  # each agent builds on the previous one
PROVIDER = None
TASK = 'Announce a schedule change for sports day.'

# (key, role, instruction)
AGENTS = [
    ('fact_collector', 'Fact Collector', 'Collect changes.'),
    ('message_writer', 'Message Writer', 'Write the message.'),
    ('translator', 'Translator', 'Adapt for languages.'),
    ('accessibility_checker', 'Accessibility Checker', 'Check readability.'),
    ('distribution_planner', 'Distribution Planner', 'Plan channels.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
