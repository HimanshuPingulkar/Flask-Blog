from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Himanshu, welcome to Flask!</h1>'