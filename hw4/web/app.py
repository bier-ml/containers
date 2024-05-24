from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World from Custom Web App!"


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    serve(app, host='0.0.0.0', port=5000)
