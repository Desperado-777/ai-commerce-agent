from .base_agent import BaseAgent

from llm.deepseek_client import DeepSeekClient


class TrendAnalysisAgent(BaseAgent):

    """
    Analyze market trend and consumer signals.
    """


    def __init__(self):

        super().__init__(
            "Trend Analysis Agent"
        )

        self.llm = DeepSeekClient()



    def run(self, input_data):

        product = input_data.get(
            "product",
            "unknown"
        )

        market = input_data.get(
            "market",
            "USA"
        )


        prompt = f"""
You are a US ecommerce trend analyst.

Analyze market trend.

Product:
{product}

Market:
{market}


Analyze:

1. Google search trend
2. TikTok opportunity
3. Amazon demand
4. Consumer pain points
5. Future growth potential
6. Trend score (0-100)

Return a business trend report.
"""


        analysis = self.llm.chat(
            prompt
        )


        return {

            "agent": self.name,

            "product": product,

            "market": market,

            "analysis": analysis

        }