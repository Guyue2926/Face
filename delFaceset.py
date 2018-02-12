from face_config import  delFaceset_httpUrl
from face_config import  serFile
from face_config import Data1
from getFaceset import getFaceset
import json
import requests

def delFaceset():
    faceset_token=getFaceset()
    data=dict(Data1())
    data["check_empty"]=0
    data["faceset_token"]=faceset_token
    print(data)
    respond = requests.post(delFaceset_httpUrl(), data=data)
    if respond.status_code == 200:
        text =(dict(json.loads(respond.text)))

    else:
        text = (dict(json.loads(respond.text)))
        print(text)


if __name__ == '__main__':
    delFaceset()

