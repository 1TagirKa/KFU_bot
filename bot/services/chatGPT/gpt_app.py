from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'XJw38X6HfR2QXj68cDd7nJH3k5g6ZzBjM5i9V9lR'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data['prompt']
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=150
        )
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)