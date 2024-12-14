from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api')
def api():
    return jsonify({"message": "Hello from Backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
