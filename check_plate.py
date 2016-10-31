from subprocess import check_output
import glob

def read_plate(filename):
    plate_dict = check_output("alpr -c eu -p nl -j %s" %filename,shell=True).decode()
    return eval(plate_dict)

list = glob.glob('sample/*.jpg')
count = 0
for item in list:
    try:
        plate = read_plate(item)['results'][0]['plate']
        count += 1
        print(plate)
    except:
        continue
