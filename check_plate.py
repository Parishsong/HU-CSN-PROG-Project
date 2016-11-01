from subprocess import check_output
import time

def getPlateInfo(filename):
    plate_dict = check_output("alpr -c eu -p nl -n 1 -j %s" %filename,shell=True).decode()
    return eval(plate_dict)

def getPlateNumber(filename):
    plate = getPlateInfo(filename)['results'][0]['plate']
    return plate

def getPlateTime(filename):
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(getPlateInfo(filename)['epoch_time'])/1000))
    return date
