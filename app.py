from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_wold():
    return 'Hello, Simple Flask application'