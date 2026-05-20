from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.core.websocket_manager import (
    manager
)

router = APIRouter(
    tags=["WebSocket"]
)


@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket
):

    await manager.connect(
        websocket
    )

    try:

        while True:

            data = await websocket.receive_text()

            await manager.broadcast(
                f"Realtime Message: {data}"
            )

    except WebSocketDisconnect:

        manager.disconnect(
            websocket
        )