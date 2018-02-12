from face_config import  getFaceset_httpUrl
from face_config import  serFile
from face_config import Data1
import json
import requests

def getFaceset():
    data=dict(Data1())
    respond = requests.post(getFaceset_httpUrl(), data=data)
    if respond.status_code == 200:
        text =(dict(json.loads(respond.text))).get("facesets")
        print("faceset_token is %s"%text[1].get("faceset_token"))
        print("outer_id is %s"%text[1].get("outer_id"))
        print("display_name is %s"%text[1].get("display_name"))
    else:
        text = (dict(json.loads(respond.text)))
        print(text)
    return (text[1].get("faceset_token"))

if __name__ == '__main__':
    getFaceset()

