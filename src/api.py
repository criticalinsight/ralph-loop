from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
async def info():
    return {"status": "operational", "agent": "Ralph"}