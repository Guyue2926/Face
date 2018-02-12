import json
import requests
import base64
from face_config import det_httpUrl

def imgFile()       :
    filePath="data/img/2.jpg"
    with open(filePath, "rb") as f:
        files = base64.b64encode(f.read())
    file={"image_base64": files}

    return file


def getToken():

    respond = requests.post(httpUrl(), data=dict(Data(),**imgFile()))
    if respond :
        text=json.loads(respond.text)
        for i in text["faces"]:
            print(i["face_token"])

    return i["face_token"]

if __name__ == '__main__':
    getToken()