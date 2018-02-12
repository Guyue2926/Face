import json
import os
import requests
import sys
from face_config import  add_httpUrl
from face_config import Data1
from detFace import detFace
import time
def getFile():
    path = "NX2"
    data = Data1()
    data["outer_id"] = "18114096650"
    for filename1 in os.listdir(path):
        if (filename1[0] != '.'):
            token=filename1[-36:-4]
            print(token)
            data["face_tokens"] = token
            respond = requests.post(add_httpUrl(), data=data)
            while respond.status_code == 200:
                try:
                    text = respond.json()
                    print(text)
                    time.sleep(3)
                    break
                except:
                    info = sys.exc_info()
                    print(info[0], ":", info[1])

if __name__ == '__main__':
    getFile()
