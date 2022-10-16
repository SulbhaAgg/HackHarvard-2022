from flask import Flask, jsonify
from flask import request
import os

app = Flask(__name__)


@app.route('/', methods=["POST"])
def index():
    content = request.get_json()
    print(content['lines'][0])
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=os.getenv("PORT", default=5000))