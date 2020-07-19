from appium import webdriver
desired_caps={
    'platformName':'Android',     #系统名称Android或IOS
    'deviceName':'127.0.0.1:62001',   #设备名称
    'platformVersion':'5.1.1',   #设备系统的版本号
    'appPackage':'com.helowin.hku',   #APP的包名"
    'appActivity':'com.helowin.hm503.activity.login.StartAct',   #APP的入口
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)