from openai import OpenAI
from settings import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-5-mini",  # يمكنك تغييره لأي نموذج في OpenRouter
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
