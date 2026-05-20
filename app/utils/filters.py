def apply_task_filters(
    query,
    Task,
    status=None,
    priority=None
):

    if status:

        query = query.filter(
            Task.status == status
        )

    if priority:

        query = query.filter(
            Task.priority == priority
        )

    return query