import openai
from config import OPENAI_API_KEY

def generate_query(prompt, max_tokens=50):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7
    )
    return response.choices[0].text.strip()
