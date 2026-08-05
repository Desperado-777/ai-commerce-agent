from fastapi import FastAPI
from pydantic import BaseModel

from agents.product_research_agent import ProductResearchAgent


app = FastAPI(
    title="AI Commerce Agent API",
    version="0.2"
)


agent = ProductResearchAgent()



class ProductRequest(BaseModel):

    product: str

    market: str = "USA"



@app.get("/")
def home():

    return {
        "message":
        "AI Commerce Agent Running"
    }



@app.post("/research")
def research(
    request: ProductRequest
):

    result = agent.run(
        {
            "product": request.product,
            "market": request.market
        }
    )

    return result