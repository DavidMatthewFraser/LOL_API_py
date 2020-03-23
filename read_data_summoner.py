import requests

def readSummoner(region, summonerName, APIKey):
    #Gets the necessary input to get information from the lol API
    responseFile = requestData(region, summonerName, APIKey)
    ID = responseFile['id']
    accountID = responseFile['accountId']
    puuid = responseFile['puuid']
    name = responseFile['name']
    profileIcon = responseFile['profileIconId']
    revisionDate = responseFile['revisionDate']
    summonerLevel = responseFile['summonerLevel']
    summonerInfo = {'ID' : ID, 'accountID' : accountID, 'PUUID' : puuid, 'Name' : name, 'profileIcon' : profileIcon, 'revisionDate' : revisionDate, 'summonerLevel' : summonerLevel}
    ##Gets all of the profile info from the JSON
    return summonerInfo

def requestData(region, summonerName, APIKey):
    API = "/?api_key="
    bulkOfURL = ".api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    https = "https://"
    URL = https + region + bulkOfURL + summonerName + API + APIKey
    response = requests.get(URL)
    return response.json()
