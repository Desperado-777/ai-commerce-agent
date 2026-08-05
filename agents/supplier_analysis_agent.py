from .base_agent import BaseAgent

from llm.deepseek_client import DeepSeekClient

from prompts.prompt_loader import load_prompt


class SupplierAnalysisAgent(BaseAgent):

    """
    Analyze supplier opportunities.
    """


    def __init__(self):

        super().__init__(
            "Supplier Analysis Agent"
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
You are a US ecommerce supplier analyst.

Analyze supplier opportunity.

Product:
{product}

Market:
{market}


Provide:

1. Best sourcing regions
2. Supplier requirements
3. MOQ estimation
4. Manufacturing cost
5. Import risks
6. Recommendation

Return business analysis.
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