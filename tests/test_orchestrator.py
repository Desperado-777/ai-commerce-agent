from agents.orchestrator import CommerceOrchestrator


system = CommerceOrchestrator()


result = system.analyze(
    "portable solar generator",
    "USA"
)


print(result)

