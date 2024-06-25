# bot_functions.py
import requests

def get_voice_response(text, tts_url):
    response = requests.post(tts_url, json={'text': text})
    if response.ok:
        return response.content
    else:
        return None