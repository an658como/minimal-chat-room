# 🗨️ Real-Time Chat Rooms with FastAPI and WebSockets

This is a **real-time chat room application** built with **FastAPI** using **WebSockets**.  
It allows multiple clients to join chat rooms and exchange messages instantly.

---

## 🚀 Features

- Multiple chat rooms (channels)
- Real-time communication using WebSockets
- Automatic broadcast to all users in the same room
- Automatic cleanup when clients disconnect
- Simple REST endpoint for health check

---

## 🧠 Project Structure

```
.
├── main.py                 # FastAPI app entry point
├── connection_manager.py   # Manages active WebSocket connections per room
└── README.md
```

---

## ⚙️ How It Works

1. **Clients connect** to `/ws/{room}` via WebSocket.
2. Each connection joins the specified room.
3. When a client sends a message, the server:
   - Receives it via the open WebSocket connection
   - Broadcasts it to all other clients in the same room
4. When a client disconnects, it is removed from the room automatically.

---

## 🧩 Example Message Flow

**Client 1 connects**
```js
let ws1 = new WebSocket("wss://<your-codespace>.app.github.dev/ws/general");
```

**Client 2 connects**
```js
let ws2 = new WebSocket("wss://<your-codespace>.app.github.dev/ws/general");
```

**Client 1 sends a message**
```js
ws1.send("Hello from client 1!");
```

**Client 2 receives**
```
Server: Hello from client 1!
```

---

## 🧰 Installation and Running

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/fastapi-chat.git
cd fastapi-chat
```

### 2️⃣ Install Dependencies
```bash
pip install fastapi uvicorn
```

### 3️⃣ Run the Server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 4️⃣ Open in Browser
Go to:
```
https://<your-codespace>.app.github.dev
```

---

## 🧪 Testing via Browser Console

1. Open your FastAPI app in the browser.
2. Open **Developer Console (F12)**.
3. Connect to WebSocket:
   ```js
   let ws = new WebSocket("wss://" + location.host + "/ws/general");
   ws.onmessage = (e) => console.log("Message:", e.data);
   ```
4. Send a message:
   ```js
   ws.send("Hello world!");
   ```

---

## 🩺 Health Check Endpoint

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/` | Returns service status |

Example:
```bash
curl https://<your-codespace>.app.github.dev/
```

Response:
```json
{ "message": "service is running" }
```

---

## 🧼 Clean Disconnect Handling

When a user disconnects:
- The WebSocket is removed from the room’s connection list
- Empty rooms are automatically deleted

---

## 💡 Notes

- Always connect from the **same origin** as your app (your Codespace domain) to avoid browser cross-origin restrictions.
- This is an in-memory application — no message persistence.
- For production, consider integrating Redis or a database for scalable room management.

---

