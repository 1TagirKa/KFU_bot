# app.py
from flask import Flask, request, jsonify
from chat_model import TechSupportChatModel

app = Flask(__name__)
chat_model = TechSupportChatModel()

@app.route('/solve', methods=['POST'])
def solve():
    error_type = request.json['error_type']
    response = chat_model.generate_response(error_type)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)