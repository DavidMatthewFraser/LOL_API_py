from flask import Flask
from flask import render_template
from read_data_summoner import *

api_key = "" # your stream key

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/profile')
@app.route('/profile/<name>')
def hello(name=None):
    name = readSummoner('NA1', name, api_key)['Name']
    profileIcon = str(readSummoner('NA1', name, api_key)['profileIcon'])
    summonerLevel = readSummoner('NA1', name, api_key)['summonerLevel']

    if(name != None):
        name = name + "'s profile'"
    return render_template('profile.html', sum_name=name, profileIcon=profileIcon, summonerLevel=summonerLevel)
