"""Disaster Response Coordinator

Task: Coordinate a flood response for a small town.
Framework: Google Agent Development Kit (ADK)
"""
from runtime import run_app

SLUG = 'disaster_response'
TITLE = 'Disaster Response Coordinator'
PATTERN = 'fanout'  # first agent plans, middle agents work in parallel, last agent merges
PROVIDER = None
TASK = 'Coordinate a flood response for a small town.'

# (key, role, instruction)
AGENTS = [
    ('situation_analyst', 'Situation Analyst', 'Assess situation.'),
    ('shelter_planner', 'Shelter Planner', 'Plan shelters.'),
    ('supply_coordinator', 'Supply Coordinator', 'Plan supplies.'),
    ('volunteer_manager', 'Volunteer Manager', 'Coordinate volunteers.'),
    ('public_information_officer', 'Public Information Officer', 'Write alerts.'),
]


def main() -> dict:
    """Run the team offline (no API key) and return {agent_key: output}."""
    return run_app(TITLE, AGENTS, TASK, PATTERN, PROVIDER)


if __name__ == "__main__":
    from common.report import show

    show(TITLE, main())
