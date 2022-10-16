from flask import Flask, jsonify
from flask import request
import os
from a import *
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/post_data', methods=["GET","POST","PUT"])
def index():
    content = request.get_json()
    print(content)
    print(content['lines'][0])
    a,b = Get_SIze(content['type'],content["cardpoints1"],content['lines'][0],content['lines'][1],content["cardpoints2"],content['lines'][2],content['lines'][3])
    return jsonify({"size": b, 'extra': a})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=os.getenv("PORT", default=5000))