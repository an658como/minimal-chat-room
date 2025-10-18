from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


# root api - health check
@app.get("/")
def read_root():
    return {"message": "service is running"}


@app.websocket("/ws/{room}")
async def websocket_endpoint(websocket: WebSocket, room):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print(f"The requested room is {room}")
            await websocket.send_text(f"Server: {data}")
    except WebSocketDisconnect:
        print("Websocket connection is disconnected")

