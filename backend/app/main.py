from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="IntelliMyAgent API",
    description="Backend API for IntelliMyAgent AI Chatbot",
    version="0.1.0"
)

app.include_router(health_router, prefix="/api")

@app.get("/")
async def root():
    return {
        "message": "Welcome to IntelliMyAgent API",
        "version":"0.1.0"
    }