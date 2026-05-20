from datetime import datetime


def predict_task_risk(
    due_date
):

    if not due_date:

        return 0

    now = datetime.utcnow()

    remaining_days = (
        due_date - now
    ).days

    if remaining_days <= 1:

        return 95

    elif remaining_days <= 3:

        return 75

    elif remaining_days <= 7:

        return 50

    else:

        return 20