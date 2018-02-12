from face_config import  getDetail_httpUrl
from face_config import  serFile
from face_config import Data1
from getFaceset import getFaceset
import json
import requests

def getDetail():
    data=dict(Data1())
    data["outer_id"]="18114096650"
    respond = requests.post(getDetail_httpUrl(), data=data)
    if respond.status_code == 200:
        text =(dict(json.loads(respond.text)))
        print("user_data is: %s \n face_tokens is: %s \n face_count is: %s" % (
            text.get("user_data"), text.get("face_tokens"), text.get("face_count")))

    else:
        text = (dict(json.loads(respond.text)))
        print(text)

if __name__ == '__main__':
    getDetail()


