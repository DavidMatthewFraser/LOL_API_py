from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/profile')
@app.route('/profile/<name>')
def hello(name=None):
    if(name != None):
        name = name + "'s profile'"
    return render_template('profile.html', name=name, random="hello")
