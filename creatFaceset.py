from face_config import  create_httpUrl
from face_config import  serFile
from face_config import Data1
from getFaceset import getFaceset
import json
import requests

def creatFaceset():
    data=dict(Data1())
    data["display_name"]="AV2017"
    data["outer_id"]="18114096650"
    data["user_data"]="Hubing607"
    respond = requests.post(create_httpUrl(), data=data)
    if respond.status_code == 200:
        text =(dict(json.loads(respond.text)))
        print("成功创建"+text)
    else:
        text = (dict(json.loads(respond.text)))
        print("错误原因：%s"%text["error_message"])

if __name__ == '__main__':
    creatFaceset()


