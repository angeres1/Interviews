from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided.'}), 400

    name = data.get('name', '').strip()
    email = data.get('email', '').strip()

    # Simulate a "real" error when the name is too long
    if len(name) > 8:
        return jsonify({'error': 'Unkown Error' }), 400  # No response body, only status code

    if not name:
        return jsonify({'error': 'Name is required.'}), 400
    if not email:
        return jsonify({'error': 'Email is required.'}), 400

    return jsonify({'message': 'Form submitted successfully!'}), 200

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)