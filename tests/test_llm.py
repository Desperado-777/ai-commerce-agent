from llm.deepseek_client import DeepSeekClient


client = DeepSeekClient()


result = client.chat(
    "Analyze motorcycle helmet market in USA"
)


print(result)
