"""City Services Assistant

Task: Report a broken streetlight and ask about bulk-waste pickup.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'city_services'
TITLE = 'City Services Assistant'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Report a broken streetlight and ask about bulk-waste pickup.'

# (key, role, instruction)
AGENTS = [
    ('request_classifier', 'Request Classifier', 'Classify requests.'),
    ('reporter_agent', 'Reporter Agent', 'File reports.'),
    ('schedule_agent', 'Schedule Agent', 'Pickup schedules.'),
    ('status_tracker', 'Status Tracker', 'Track status.'),
    ('notifier', 'Notifier', 'Confirm to citizen.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
