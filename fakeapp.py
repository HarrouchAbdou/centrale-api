from flask import Flask, request, jsonify
app = Flask(__name__)


# A welcome message to test our server
@app.route('/')
def index():
    return "hello hamid "

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True)