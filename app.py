from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


client = MongoClient(
    'mongodb+srv://eunshu12:Mulberry1!@cluster0.x4jop40.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/127",  methods=["POST"])
def web_127_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    doc = {
        'url': url_receive,
        'star': star_receive,
        'comment': comment_receive
    }
    db.nct.insert_one(doc)

    return jsonify({'msg': '등록완료!'})


@app.route("/127", methods=["GET"])
def web_127_get():
    nct_list = list(db.nct.find({}, {'_id': False}))
    return jsonify({'ncts': nct_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
