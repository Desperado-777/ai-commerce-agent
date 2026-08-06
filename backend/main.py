from fastapi import FastAPI
from pydantic import BaseModel

from agents.orchestrator import CommerceOrchestrator


app = FastAPI(
    title="AI Commerce Agent API"
)


class ProductRequest(BaseModel):

    product: str
    market: str = "USA"



@app.get("/")
def home():

    return {
        "message":
        "AI Commerce Agent Running"
    }



@app.post("/analyze")
def analyze(
    request: ProductRequest
):

    orchestrator = EcommerceOrchestrator()


    result = orchestrator.run(
        {
            "product": request.product,
            "market": request.market
        }
    )


    return result