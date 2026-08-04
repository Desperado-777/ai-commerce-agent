from fastapi import FastAPI
from agents.product_research_agent import ProductResearchAgent


app = FastAPI(
    title="AI Commerce Agent API",
    version="0.1"
)


agent = ProductResearchAgent()


@app.get("/")
def root():
    return {
        "message": "AI Commerce Agent API running"
    }


@app.post("/research-product")
def research_product(data: dict):

    result = agent.run(data)

    return result