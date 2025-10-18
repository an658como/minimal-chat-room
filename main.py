from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from connection_manager import ConnectionManager

app = FastAPI()
connection_manager = ConnectionManager()


# root api - health check
@app.get("/")
def read_root():
    return {"message": "service is running"}


@app.get("/chat/{room}")
def get_chat_page(room: str = "general"):
    html_content = f"""
    <html>
      <body>
        <script>
          const ws = new WebSocket("wss://" + location.host + "/ws/{room}");
          ws.onopen = () => console.log("Connected!");
          ws.onmessage = (e) => console.log("Message:", e.data);
        </script>
      </body>
    </html>
    """
    return HTMLResponse(html_content)



@app.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room):
    await connection_manager.connect(websocket=websocket, room=room)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"The requested room is {room}")
            await connection_manager.broadcast(room=room, message=f"Server: {data}")
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket=websocket, room=room)
        print("Websocket connection is disconnected")

