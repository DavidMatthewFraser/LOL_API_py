from flask import Flask
from flask import render_template
from read_data_summoner import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/profile')
@app.route('/profile/<name>/<api_key>')
def hello(name=None,api_key=None):
    name = readSummoner('NA1', name, api_key)['Name']
    profileIcon = str(readSummoner('NA1', name, api_key)['profileIcon'])
    summonerLevel = readSummoner('NA1', name, api_key)['summonerLevel']

    return render_template('profile.html', sum_name=name, profileIcon=profileIcon, summonerLevel=summonerLevel)
