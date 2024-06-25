import openai

class TechSupportChatModel:
    def __init__(self):
        openai.api_key = 'XJw38X6HfR2QXj68cDd7nJH3k5g6ZzBjM5i9V9lR'

    def generate_response(self, error_type):
        prompt = self.create_prompt(error_type)
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def create_prompt(self, error_type):
        # Ваша логика для создания подходящего запроса
        return f"Помощь в решении технической проблемы: {error_type}. Какие шаги следует предпринять?"