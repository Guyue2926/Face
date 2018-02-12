import os
import requests
import sys
import faceDetect
from face_config import Data1
from PIL import Image,ImageDraw,ImageFont

def httpUrl():
    http_url = "https://api-cn.faceplusplus.com/facepp/v3/search"
    return http_url
def imgFile():
    data=Data1()
    data["outer_id"]="18114096650"
    data["image_url"]="http://9c9vimg.yuanchandi.org:8086/201703/0750195048971864.jpg"
    print(data)
    respond = requests.post(httpUrl(), data=data)
    while respond.status_code == 200:
        try:
            text = dict(respond.json())["results"]
            print("相似度：%s 图片名称：%s.jpg" % (text[0]["confidence"], text[0]["face_token"]))
            for filename1 in os.listdir("NX2"):
                filename1 = "NX2" + '/' + filename1
                if text[0]["face_token"] in filename1:
                    im = Image.open(filename1)
                    draw = ImageDraw.Draw(im)
                    draw.text((40,40),str(text[0]["confidence"]))
                    im.show()
            break
        except:
            info = sys.exc_info()
            print(info[0], ":", info[1])

def main():
    print(imgFile())

if __name__ == '__main__':
    main()