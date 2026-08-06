from .product_research_agent import ProductResearchAgent
from .supplier_analysis_agent import SupplierAnalysisAgent
from .trend_analysis_agent import TrendAnalysisAgent


class CommerceOrchestrator:
    """
    Coordinate multiple AI agents.
    """


    def __init__(self):

        self.product_agent = (
            ProductResearchAgent()
        )

        self.supplier_agent = (
            SupplierAnalysisAgent()
        )

        self.trend_agent = (
            TrendAnalysisAgent()
        )


    def analyze(
        self,
        product,
        market="USA"
    ):

        input_data = {

            "product": product,

            "market": market

        }


        product_result = (
            self.product_agent.run(
                input_data
            )
        )


        supplier_result = (
            self.supplier_agent.run(
                input_data
            )
        )


        trend_result = (
            self.trend_agent.run(
                input_data
            )
        )


        return {

            "product_analysis":
                product_result,

            "supplier_analysis":
                supplier_result,

            "trend_analysis":
                trend_result

        }
    
