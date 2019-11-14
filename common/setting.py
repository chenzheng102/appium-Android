
from appium import webdriver
def android_config(caps):
    desired_caps={}
    desired_caps['platformName']='Android'     #系统名称
    desired_caps['platformVersion']=caps["platformVersion "]  #系统的版本号
    desired_caps['deviceName']=caps["deviceName"]     #设备名称，这里是虚拟机，这个没有严格的规定
    desired_caps['udid']= caps["udid"]   #设备唯一标示
    desired_caps['appPackage']= caps["appPackage"]    #APP包名
    desired_caps['appActivity']=caps["appActivity"]       #APP入口的activity
    # driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    return desired_caps

def ios_config(caps):
    desired_caps = {"deviceName": "iPhone 6s",
      "platformName": "ios",
      "udid":caps["udid"],
      "automationName": "XCUITest",
      "xcodeOrgId":   caps["xcodeOrgId"],
      "xcodeSigningId": caps["xcodeSigningId"],
      "no-reset": caps["reset"],
      "startIWDP": caps["startIWDP"],
      "bundleId": caps["bundleId"]
        }
    return desired_caps

def web_config(caps):
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('http://www.baidu.com/')
