from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import random
import time

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulate real-time metrics for 3 demo servers
async def fetch_metrics():
    demo_monitors = []
    for i in range(1, 4):
        demo_monitors.append({
            "id": i,
            "name": f"Server-{i}",
            "host": f"192.168.1.{i}",
            "port": 10000 + i,
            "metrics": {
                "cpu": round(random.uniform(0, 100), 2),
                "memory": round(random.uniform(0, 32), 2),
                "disk": round(random.uniform(0, 1000), 2),
                "status": random.choice(["OK", "WARN", "ERROR"]),
                "last_updated": time.strftime("%Y-%m-%d %H:%M:%S")
            }
        })
    return demo_monitors

@app.websocket("/ws/metrics")
async def websocket_metrics(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            metrics = await fetch_metrics()
            await websocket.send_json(metrics)
            await asyncio.sleep(2)
    except WebSocketDisconnect:
        print("Metrics WebSocket client disconnected")

# Simulate real-time alerts/events
@app.websocket("/ws/random")
async def websocket_random(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = {
                "event": random.choice(["ALERT", "INFO", "ERROR"]),
                "value": random.randint(1, 100),
                "message": random.choice([
                    "CPU spike detected",
                    "Disk usage normal",
                    "Memory warning",
                    "Network latency high",
                    "All systems operational"
                ]),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            await websocket.send_json(data)
            await asyncio.sleep(3)
    except WebSocketDisconnect:
        print("Random WebSocket client disconnected")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
