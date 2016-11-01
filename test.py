import plate, time

plateInfo = plate.getPlateInfo('sample\\1.jpg') #Deze regel is heel belangrijk. Hier mee hoef je de API maar een keer aan te spreken voor wat je wil doen.

print(plate.getPlateNumber(plateInfo))
print(plate.getPlateTime(plateInfo)) #in unix timestamp

tijd = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(plate.getPlateTime(plateInfo)))
print(tijd)
