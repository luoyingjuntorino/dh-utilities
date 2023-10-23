from flask import Flask, render_template

app = Flask(__name__)

@app.route('/grafana')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='192.168.1.13', port=8000)

