from flask import Flask, jsonify, request, json

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def home():
    # Display all the todos in the database
    return "hello, world"


if __name__ == '__main__':
    app.run()
