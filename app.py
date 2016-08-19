from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name="TreeHouse"):
    return render_template('register.html', name=name)


@app.route('/save', methods=['POST'])
def save():
    return "<h1>Name saved!</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
