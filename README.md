# Hertzbeat Real-Time Monitoring App

A simple real-time monitoring dashboard using [Apache Hertzbeat](https://hertzbeat.com/) and Python FastAPI. The frontend is built with HTML, CSS, and JavaScript for instant metric updates.

---

## Features
- Real-time metrics from Hertzbeat
- Simple, modern dashboard UI
- Python FastAPI backend (WebSocket streaming)
- Easy setup and usage

---

## Prerequisites
- Python 3.12+
- Node.js (optional, only if you want to use npm for frontend tooling)
- Apache Hertzbeat running locally ([Quick Start Guide](https://hertzbeat.com/docs/quick-start/))

---

## Setup Instructions

### 1. Start Apache Hertzbeat
- Download and run Hertzbeat as per the [official docs](https://hertzbeat.com/docs/quick-start/).
- Ensure the REST API is available at `http://localhost:1157`.

### 2. Backend Setup (FastAPI)
1. Open a terminal in the backend folder:
   ```bash
   cd c:\Users\Supreeth\codes\hertzbeat-monitoring-app\backend
   python -m venv venv
   # Activate the virtual environment
   source venv/bin/activate   # On Windows: venv/Scripts/activate
   pip install -r requirements.txt
   ```
2. Start the FastAPI server:
   ```bash
   python main.py
   ```
   OR
   ```bash
   uvicorn main:app --reload
   ```
   - The backend will run at `http://localhost:8000`.
   - WebSocket endpoints:
     - `/ws/metrics` for real-time server metrics
     - `/ws/random` for live events & alerts

### 3. Frontend Usage
- Open `frontend/index.html` in your browser.
- The dashboard will auto-connect to the backend and display live metrics.

---

## File Structure
```
├── backend/
│   │── main.py            # FastAPI backend
│   └── requirements.txt   # Python dependencies
└── frontend/
    └── index.html         # Real-time dashboard UI
```

---

## Troubleshooting
- **Hertzbeat not running?** Make sure the service is started and accessible at `http://localhost:1157`.
- **WebSocket not connecting?** Ensure FastAPI is running and your browser allows WebSocket connections to `localhost:8000`.
- **Metrics not updating?** Check Hertzbeat API and backend logs for errors.

---

## Customization
- Edit `main.py` to change polling interval or API endpoints.
- Style or extend `frontend/index.html` for more advanced visualizations.

---

## License
MIT
