import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class DeepSeekClient:

    def __init__(self):

        api_key = os.getenv(
            "DEEPSEEK_API_KEY"
        )

        self.client = OpenAI(
            api_key="sk-d5d728d3d81f43e3853b9b9dc3dba3c3",
            base_url="https://api.deepseek.com"
        )


    def chat(self, prompt):

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content