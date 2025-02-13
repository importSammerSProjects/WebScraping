import functions as f
from flask import Flask, jsonify, request
import json

# print(f.getPost('https://public.app/video/sp_l0ey8w6tsphks'))
# d = json.loads(f.getFeed('MH_LA_UDGIR'))
# f.getNext('MH_LA_UDGIR', 'sp_l0ey8w6tsphks')

# The functions /getPost, /getFeed, /getNext returns a json object as response so you should convert it before use

app = Flask(__name__)


@app.route('/getpost', methods=['GET', 'POST'])
def resone():
    return jsonify({'data': f.getPost(str(request.args.get("u")))}), 200

@app.route('/getfeed', methods=['GET', 'POST'])
def restwo():
    return jsonify({'data': f.getFeed(str(request.args.get("d")))}), 200

@app.route('/getnext', methods=['GET', 'POST'])
def resthree():
    return jsonify({'data': f.getNext(str(request.args.get("d")), str(request.args.get("d")))}), 200


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8080)