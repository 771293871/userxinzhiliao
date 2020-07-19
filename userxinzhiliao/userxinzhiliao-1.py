#coding=utf-8
from appium import webdriver
import time
#模拟器
desired_caps={
    'platformName':'Android',     #系统名称Android或IOS
    'deviceName':'127.0.0.1:62001',   #设备名称
    'platformVersion':'5.1.1',   #设备系统的版本号
    'appPackage':'com.helowin.hku',   #APP的包名"
    'appActivity':'com.helowin.hm503.activity.login.StartAct',   #APP的入口
}
#wqw的华为noua3
# desired_caps={
#     'platformName':'Android',     #系统名称Android或IOS
#     'deviceName':'DRB5T18807003509',   #设备名称
#     'platformVersion':'9',   #设备系统的版本号
#     'appPackage':'com.helowin.hku',   #APP的包名"
#     'appActivity':'com.helowin.hm503.activity.login.StartAct',   #APP的入口
# }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(5)
# #获得手机的屏幕尺寸x,y
def getsize():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return (x,y)
#向左滑动屏幕
def swipleft(t):
    l=getsize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    driver.swipe(x1,y1,x2,y1,t)
swipleft(1000)
swipleft(1000)

#通过id定位输入框并输入内容
#def byidsend(id):

#driver.find_element_by_class_name("android.widget.EditText").send_keys("15257181529")







