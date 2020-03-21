import requests

def read_data_leauge(region, encryptedSummonerID, APIKey):
    #Accesses the information from the LOL API
    responseFile = requestDataLeauge(region, encryptedSummonerID, APIKey)
    print(responseFile)
def requestDataLeauge(region, encryptedSummonerID, APIKey):
    API = "/?api_key="
    bulkOfURL = ".api.riotgames.com/lol/league/v4/entries/by-summoner/"
    https = "https://"
    URL = https + region + bulkOfURL + encryptedSummonerID + API + APIKey
    response = requests.get(URL)
    return response.json()
