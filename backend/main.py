from fastapi import FastAPI


app = FastAPI(
    title="AI Commerce Agent API",
    description="AI-powered cross-border commerce system",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Commerce Agent is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }