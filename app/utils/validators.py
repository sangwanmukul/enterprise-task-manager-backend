VALID_ROLES = [
    "SUPER_ADMIN",
    "PROJECT_MANAGER",
    "TEAM_LEAD",
    "DEVELOPER",
    "VIEWER"
]

VALID_TASK_STATUS = [
    "BACKLOG",
    "TODO",
    "IN_PROGRESS",
    "IN_REVIEW",
    "TESTING",
    "DONE",
    "BLOCKED"
]

VALID_PRIORITIES = [
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL"
]


def validate_role(role: str):

    return role in VALID_ROLES


def validate_status(status: str):

    return status in VALID_TASK_STATUS


def validate_priority(priority: str):

    return priority in VALID_PRIORITIES