def paginate(
    query,
    page: int,
    limit: int
):

    total = query.count()

    items = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {

        "total": total,

        "page": page,

        "limit": limit,

        "data": items
    }