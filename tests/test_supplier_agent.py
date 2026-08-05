from agents.supplier_analysis_agent import SupplierAnalysisAgent


agent = SupplierAnalysisAgent()


result = agent.run(
    {
        "product":
        "portable solar generator",

        "market":
        "USA"
    }
)


print(result)