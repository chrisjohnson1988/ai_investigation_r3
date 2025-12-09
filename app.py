from flask import Flask, jsonify
from logger import Logging

app = Flask(__name__)
logger = Logging(level='DEBUG')

@app.route('/hello', methods=['GET'])
def hello_world():
    logger.log("Hello World endpoint was called", level='INFO')
    return jsonify({"message": "Hello World"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
