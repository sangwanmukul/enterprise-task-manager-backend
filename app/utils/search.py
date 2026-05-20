def apply_task_search(
    query,
    keyword,
    Task
):

    if keyword:

        query = query.filter(

            Task.title.ilike(f"%{keyword}%")
        )

    return query