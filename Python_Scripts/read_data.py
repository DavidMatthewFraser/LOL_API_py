import requests

def main():
    print("Enter your region (NA1 EUW EUNE LAN BR KR LAS OCE TR RU PBE) to get started\n")
    region = input()
    print("Now, enter your summoners name without spaces /n")
    summonerName = input()
    print("Copy and paste your API Key here: /n")
    APIKey = input()
    #Gets the necessary input to get information from the lol API
    responseFile = requestData(region, summonerName, APIKey)
    print(responseFile)
    
def requestData(region, summonerName, APIKey):
    API = "/?api_key="
    bulkOfURL = ".api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    https = "https://"
    URL = https + region + bulkOfURL + summonerName + API + APIKey
    response = requests.get(URL)
    return response.json()
