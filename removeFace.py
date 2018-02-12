import json
import requests
import string
from face_config import  removeFace_httpUrl
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
def faceRemove():
    tokens=getToken()
    data=Data1()
    data["outer_id"]="13889292926"
    data["face_tokens"]="RemoveAllFaceTokens"
    print(data)
    respond = requests.post(removeFace_httpUrl(), data=data)
    if respond.status_code == 200:
        text = (dict(json.loads(respond.text)))
        print("数据总数 is: %s \n 删除数量 is: %s \n 错误信息 is: %s" % (
            text.get("face_count"), text.get("face_removed"), text.get("failure_datail")))
    else:
        text = (dict(json.loads(respond.text)))
        print(text)
if __name__ == '__main__':
    faceRemove()