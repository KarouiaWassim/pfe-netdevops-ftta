from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from starlette.responses import Response

app = FastAPI()

REQUEST_COUNT = Counter("request_count", "Total API requests")

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    return {"message": "NETDEVOPS API OK"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")