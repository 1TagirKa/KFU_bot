from flask import Flask, request, send_file
from gtts import gTTS
import tempfile

app = Flask(__name__)

@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data['text']
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        tts = gTTS(text, lang='ru')
        tts.save(temp_file.name)
        return send_file(temp_file.name, attachment_filename='speech.mp3')
    finally:
        temp_file.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)