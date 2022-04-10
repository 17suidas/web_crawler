# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from asyncio.windows_events import NULL
from seleniumwire import webdriver  
import time
import re
from seleniumwire.utils import decode

def GeetestUrl():
    options=webdriver.FirefoxOptions()
    browser=webdriver.Firefox(options=options)
    # browser=webdriver.Firefox(executable_path='E:\大创\代码\爬取验证码代码\GeckoDriver\geckodriver.exe')  #括号中的也是非典型的安装firefox驱动的方法,常规的方法我一直试的不行,但这种方法包管行.

    #存储链接的空表
    down1=set()
    down2=[]

    #匹配验证码图片连接的正则表达式，得到的结果仅括号的部分
    mtch1=re.compile(r'https://static.geetest.com/captcha_v3/batch/v3/(2021-12-02T15|2021-10-26T17|2021-10-27T18)/word(.*?).jpg') #####注：正则表达式里的日期随时变化，及时更改
    # mtch2=re.compile(r'https://static.geetest.com/captcha_v3/batch/v3/2021-08-31T12/word(.*?).jpg')

    browser.get('https://passport.bilibili.com/register/phone.html?from_spm_id=333.851.top_bar.login_window#/phone') #输入你的目标网址
    time.sleep(3) #打开网址后休息3秒钟,可用可不用
    # browser.find_element_by_xpath('//*[@id="6"]/td[4]').click() #找到想要点击的元素,然后进行点击动作,让窗口弹出来


    #输入昵称
    browser.find_element_by_xpath("//body/div[@id='app']/div[2]/div[3]/form[1]/div[1]/div[1]/input[1]").send_keys("ninininiyao1")
    #输入密码
    browser.find_element_by_xpath("//body/div[@id='app']/div[2]/div[3]/form[1]/div[3]/div[1]/input[1]").send_keys("mimashi123")
    #输入“电话号码”
    browser.find_element_by_xpath("//body/div[@id='app']/div[2]/div[3]/form[1]/div[5]/div[1]/input[1]").send_keys("12345678910")
    #点击“点击获取”
    browser.find_element_by_xpath("//span[contains(text(),'点击获取')]").click()


    i=0#刷新键按第六次时会提示频繁，需点击“请点击此处重试”,i做计数器
    x=0
    while x < 50:
        print(x+1)
        #等待
        time.sleep(0.5)
        #点击刷新按钮以获得ajax请求
        WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//body/div[2]/div[2]/div[6]/div[1]/div[1]/div[3]/div[1]/a[2]"))).click()
        i+=1
        x+=1
        if(i!=6):
            for request in browser.requests:
                if request.response:
                    result=re.findall(mtch1,str(request))
                    if result !=[]:
                        name =  result[0][0]+'/word'+result[0][1]
                        down1.add(name)
                            # print(down)
                        # print(type(str(request)))
                        # i+=1
                        # time.sleep(0.5)   #等待0.5秒
        else:
            WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'请点击此处重试')]"))).click()
            i=0
            time.sleep(0.4)

    #去重
    # down2=[list(t) for t in set(tuple(_) for _ in down1)]
    print('去重后:')
    for item in down1:
        print(item)
    browser.quit()
    return down1
