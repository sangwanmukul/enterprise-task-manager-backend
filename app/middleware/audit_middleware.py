from starlette.middleware.base import (
    BaseHTTPMiddleware
)


class AuditMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next
    ):

        print(
            f"AUDIT => {request.method} {request.url}"
        )

        response = await call_next(
            request
        )

        return response