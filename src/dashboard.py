from fastapi import FastAPI
from .health_checker import HealthChecker
import uvicorn

app = FastAPI()
health = HealthChecker()

@app.get("/api/health")
def get_health():
    return health.generate_health_report()

@app.get("/api/servers")
def get_servers():
    return {"servers": []}

@app.get("/api/alerts")
def get_alerts():
    return {"alerts": []}

@app.get("/api/vms")
def get_vms():
    return {"vms": []}
