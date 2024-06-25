from flask import Flask, request, jsonify
from openai_client import generate_query

app = Flask(__name__)


@app.route('/generate_query', methods=['POST'])
def handle_generate_query():
    data = request.json
    context = data.get('context')
    if not context:
        return jsonify({'error': 'Context parameter is required'}), 400

    generated_query = generate_query(context)
    return jsonify({'generated_query': generated_query})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
