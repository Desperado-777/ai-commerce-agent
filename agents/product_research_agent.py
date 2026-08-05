from .base_agent import BaseAgent

from llm.deepseek_client import DeepSeekClient

from prompts.prompt_loader import load_prompt


class ProductResearchAgent(BaseAgent):
    """
    AI Agent for product opportunity research.
    """


    def __init__(self):

        super().__init__(
            "Product Research Agent"
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


        template = load_prompt(
            "product_research_prompt.txt"
        )


        prompt = template.format(
            product=product,
            market=market
        )


        analysis = self.llm.chat(
            prompt
        )


        return {
            "agent": self.name,
            "product": product,
            "market": market,
            "analysis": analysis
        }