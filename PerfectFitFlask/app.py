from flask import Flask, jsonify
from flask import request
import os
from a import *

app = Flask(__name__)


@app.route('/', methods=["POST"])
def index():
    content = request.get_json()
    print(content['lines'][0])
    Get_SIze(content['type'],cardPoints1,content['lines'][0],content['lines'][1],cardPoints2,content['lines'][2],content['lines'][3])
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=os.getenv("PORT", default=5000))