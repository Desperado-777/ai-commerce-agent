from agents.orchestrator import EcommerceOrchestrator


system = EcommerceOrchestrator()


result = system.analyze(
    "portable solar generator",
    "USA"
)


print(result)

