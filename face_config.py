import os
import base64
import requests
import json
import time
import sys

def det_httpUrl():
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    return http_url
def add_httpUrl():
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/addface"
    return http_url
def removeFace_httpUrl():
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface"
    return http_url
def getDetail_httpUrl():
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail" #查询faceset 详细信息
    return http_url
def create_httpUrl():
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create" #创建faceset
    return http_url
def getFaceset_httpUrl():
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets" #获取faceset信息
    return http_url
def delFaceset_httpUrl():
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/delete"
    return http_url
# def removeFace_httpUrl():
#     http_url = " https://api-cn.faceplusplus.com/facepp/v3/faceset/removeface"
#     return http_url
def Data1():
    #数据准备
    key = "mISAQbFPGcV6mUSVFPoa3XpSnFv-lJ4B"
    secret = "fXg12-LbceQ2plKOn32NPLdpqqxXcjtK"
    data = {"api_key":key, "api_secret":secret}
    return data
def Data2():
    #数据准备
    key = "mYB10MRNDxzw23tckuW8bb-tL2ACU5N_"
    secret = "SwRrOx7ok-XUf42lq8M5Fen3yZ_5P1ix"
    data = {"api_key":key, "api_secret":secret,"return_landmark":1}
    return data
def serFile():
    path="data/images"
    token = []
    for filename1 in os.listdir(path):
        if (filename1[0] != '.'):
            if not filename1:
                break
            filename1 = path + '/' + filename1
            respond=imgPost(filename1)
            if respond.status_code == 200:
                text = (dict(json.loads(respond.text)))["faces"]

                for i in text:
                    p = i["face_token"]
                    p1 = open("token", "a+")
                    p1.write(",")
                    p1.write(p)
                    p1.close()

                time.sleep(2)
            else:
                print(respond.__init__)
    return (token)
def imgPost(filename):
    f = open(filename, "rb")
    files = base64.b64encode(f.read())
    data=Data1()
    data["image_base64"]=files
    respond = requests.post(det_httpUrl(), data=data)
    while respond.status_code == 200:
        try :
            pass
        except:
            info = sys.exc_info()
            print( info[0], ":", info[1])

    f.close()
    return (respond.status_code)


if __name__ == '__main__':
    serFile()
#     print(serFile())