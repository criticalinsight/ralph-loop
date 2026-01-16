from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
async def info():
    return {
        "app_name": "Ralph API",
        "version": "1.0.0",
        "status": "operational",
        "agent": "Ralph"
    }