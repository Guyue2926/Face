import json
import requests
from face_config import Data1
from face_config import create_httpUrl


def creatFaceset():
    # data=dict(Data1())
    data={"display_name":"Test2017","outer_id":"13889292926","user_data":"Test"}
    data=dict(Data1(),**data)
    respond = requests.post(create_httpUrl(), data=data)
    if respond.status_code == 200:
        text =(dict(json.loads(respond.text)))
        print("成功创建"+text)
    else:
        text = (dict(json.loads(respond.text)))
        print("错误原因：%s"%text["error_message"])

if __name__ == '__main__':
    creatFaceset()


