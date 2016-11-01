import requests, json
from auth import openALPRSecretkey as key

def getPlateInfo(filename):
    private_key = key
    url = "https://api.openalpr.com/v1/recognize?secret_key={}&tasks=plate&country=eu".format(private_key)
    file = open(filename, 'rb')
    response = requests.post(url, files={'image': file})
    jsontext = json.loads(response.text)
    return jsontext

def getPlateNumber(plateInfo):
    plate = plateInfo['plate']['results'][0]['plate']
    return plate

def getPlateTime(plateInfo):
    date = int(plateInfo['plate']['epoch_time']/1000)
    return date
