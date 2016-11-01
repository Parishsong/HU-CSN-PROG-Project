import requests, json, time
from auth import key

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
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(plateInfo['plate']['epoch_time'])/1000))
    return date
