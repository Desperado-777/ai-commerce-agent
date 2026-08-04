from agents.product_research_agent import ProductResearchAgent


agent = ProductResearchAgent()


result = agent.run(
    {
        "product": "motorcycle helmet",
        "market": "USA"
    }
)


print(result)