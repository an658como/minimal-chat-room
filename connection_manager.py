from collections import defaultdict

from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.active_connections = defaultdict(set)

    
    async def connect(self, websocket: WebSocket, room: str):
        await websocket.accept()
        self.active_connections[room].add(websocket)

    
    def disconnect(self, websocket: WebSocket, room: str):
        self.active_connections[room].discard(websocket)

        # delete empty rooms
        if not self.active_connections[room]:
            del self.active_connections[room]

    async def broadcast(self, room :str, message: str):
        for connection in self.active_connections[room]:
            try:
                await connection.send_text(message)
            except Exception:
                # remove any broken connections automatically
                self.disconnect(connection, room)