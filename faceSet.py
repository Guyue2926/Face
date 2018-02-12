import json
import requests
import base64
import time
import string
from face_config import  det_httpUrl
from face_config import  create_httpUrl
from face_config import  serFile
from face_config import Data1

def getToken():
    File=serFile()
    print(File)
def getToken():
    path="token"
    f=open(path,"rb")
    text = f.read()
    text=str(text,encoding='utf-8')
    token=text.strip(string.punctuation)
    return token
    f.close()
def faceSet():
    face_tokens=getToken()
    face_tokens={"face_tokens":face_tokens}
    data=dict(Data1(),**(face_tokens))
    print(data)
    respond = requests.post(create_httpUrl(), data=data)
    if respond.status_code == 200:
        text = (dict(json.loads(respond.text)))
        print(text)
    else:
        text = (dict(json.loads(respond.text)))
        print(text)
def main():
    faceSet()
if __name__ == '__main__':
    main()

