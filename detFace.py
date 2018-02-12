import json
import requests
import sys
from face_config import Data1
from face_config import det_httpUrl
import os
import base64
import time

path = "NX"
token = []
def detFace():
    for filename1 in os.listdir(path):
        if (filename1[0] != '.'):
            filename1 = path + '/' + filename1
            print(filename1)
            f = open(filename1, "rb")
            files = base64.b64encode(f.read())
            data = Data1()
            data["image_base64"] = files
            respond = requests.post(det_httpUrl(), data=data)
            f.close()
            while respond.status_code == 200:
                try:
                    text=respond.json()["faces"][0]
                    print(text["face_token"])
                    os.rename(filename1,filename1[:-4]+text["face_token"]+".jpg")
                    time.sleep(3)
                    break
                except:
                    info = sys.exc_info()
                    print(info[0], ":", info[1])
    return text

if __name__ == '__main__':
    detFace()


