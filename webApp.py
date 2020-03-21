from flask import Flask
from flask import render_template
from read_data_summoner import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/profile')
@app.route('/profile/<name>')
def hello(name=None):
    name = readSummoner('NA1', name, 'RGAPI-fb4acaba-bdef-451b-9ceb-33b234d0bb6d')['Name'];
    profileIcon = readSummoner('NA1', name, 'RGAPI-fb4acaba-bdef-451b-9ceb-33b234d0bb6d')['profileIcon'];
    summonerLevel = readSummoner('NA1', name, 'RGAPI-fb4acaba-bdef-451b-9ceb-33b234d0bb6d')['summonerLevel'];

    if(name != None):
        name = name + "'s profile'"
    return render_template('profile.html', name=name, profileIcon=profileIcon, summonerLevel=summonerLevel)
