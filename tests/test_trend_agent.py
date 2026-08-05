from agents.trend_analysis_agent import TrendAnalysisAgent


agent = TrendAnalysisAgent()


result = agent.run(
    {
        "product":
        "portable solar generator",

        "market":
        "USA"
    }
)


print(result)