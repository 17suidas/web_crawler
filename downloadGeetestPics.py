import requests
# import urllib.request,urllib.response
# from requests.models import Response
from getGeetestUrl import  GeetestUrl
import os


def download(url):
    i = 0
    for j in range(50):
        s = requests.session()
        s.keep_alive = False
        down = GeetestUrl()
        for item in down:
            response=requests.get(url + item +'.jpg',  timeout=5)
            print(item+'.jpg',response.status_code,response.reason) #200表示请求成功
            try:
                name = item[item.rfind('/'):]
                if 'geetest'+'/'+ name +'.jpg' in os.listdir('geetest'):
                    print('已存在')
                with open('2021-12-02T15'+'/'+ name +'.jpg',mode='wb') as file:       #图片保存到当前目录
                    file.write(response.content)
                    i+=1
                    print(i)
                    print("图片保存成功！")
            except:
                print("图片保存失败！")
        s.close()

url="https://static.geetest.com/captcha_v3/batch/v3/"   #验证码的网址

if __name__ == '__main__':
    download(url)