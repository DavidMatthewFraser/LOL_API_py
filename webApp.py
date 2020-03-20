from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/profile')
@app.route('/profile/<name>')
def hello(name=None):
    return render_template('profile.html', name=name)
