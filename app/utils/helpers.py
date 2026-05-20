from datetime import datetime


def calculate_completion_rate(
    completed_tasks,
    total_tasks
):

    if total_tasks == 0:
        return 0

    return round(
        (completed_tasks / total_tasks) * 100,
        2
    )


def format_datetime(dt):

    if not dt:
        return None

    return dt.strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def generate_response(
    success: bool,
    message: str,
    data=None
):

    return {
        "success": success,
        "message": message,
        "data": data
    }


def is_overdue(due_date):

    if not due_date:
        return False

    return due_date < datetime.utcnow()