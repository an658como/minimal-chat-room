import pytest

from mock_web_socket import MockWebSocket
from connection_manager import ConnectionManager


@pytest.fixture
def connection_manger():
    return ConnectionManager()

@pytest.mark.asyncio
async def test_connect(connection_manger):
    ws = MockWebSocket()
    await connection_manger.connect(websocket=ws, room="sample room")

    assert ws.accepted == True
    assert "sample room" in connection_manger.active_connections