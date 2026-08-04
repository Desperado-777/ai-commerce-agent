class BaseAgent:
    """
    Base class for all AI Agents.
    """

    def __init__(self, name):
        self.name = name


    def run(self, input_data):
        """
        Execute agent task.

        Every child agent must override this method.
        """
        raise NotImplementedError(
            "Agent must implement run() method"
        )