from flask import Flask
from flask import Flask, render_template, request
from flask import jsonify
from datetime import datetime


def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/')
def index():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return 'hello, timestamp is:' + str(formatted_datetime)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

