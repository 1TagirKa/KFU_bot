import requests

def get_chatgpt_response(prompt, chatgpt_url):
    response = requests.post(chatgpt_url, json={'prompt': prompt})
    if response.ok:
        return response.json()
    else:
        return None