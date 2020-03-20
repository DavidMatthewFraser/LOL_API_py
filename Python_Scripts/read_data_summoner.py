import requests

def main():
    print("Enter your region (NA1 EUW1 EUN1 LA1 LA2 JP1 OC1 BR1 KR RU) to get started")
    region = input()
    print("Now, enter your summoners name without spaces")
    summonerName = input()
    print("Copy and paste your API Key here: /n")
    APIKey = input()
    #Gets the necessary input to get information from the lol API
    responseFile = requestData(region, summonerName, APIKey)
    ID = responseFile['id']
    accountID = responseFile['accountId']
    puuid = responseFile['puuid']
    name = responseFile['name']
    profileIcon = responseFile['profileIconId']
    revisionDate = responseFile['revisionDate']
    summonerLevel = responseFile['summonerLevel']
    
def requestData(region, summonerName, APIKey):
    API = "/?api_key="
    bulkOfURL = ".api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    https = "https://"
    URL = https + region + bulkOfURL + summonerName + API + APIKey
    response = requests.get(URL)
    return response.json()
