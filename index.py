from pydoc import doc
from flask import Flask, request, jsonify
from search import search, document_index


app = Flask(__name__)


@app.route('/<q>', methods=['GET'])
def home(q):
    res = search(q)
    return jsonify(res)


@app.route('/index', methods=['POST'])
def index():
    content = request.json
    document_index(content)
    return content[0]["title"]


if __name__ == '__main__':
    app.run()
