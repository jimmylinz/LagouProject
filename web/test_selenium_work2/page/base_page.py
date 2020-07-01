import os

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

class BasePage():
    _base_url = ""
    browser = os.getenv("browser")
    def __init__(self,driver_base:WebDriver = None):
        if driver_base == None:
            # 实例化option
            option = Options()
            # 需要和启动命令的端口号一致
            option.debugger_address = "localhost:9222"
            #多浏览器处理
            browser = os.getenv("browser")
            if browser == 'firefox':
                self.driver = webdriver.Firefox
            elif browser == 'headless':
                self.driver = webdriver.PhantomJS
            elif browser == 'safari':
                self.driver = webdriver.Safari
            else:
                self.driver = webdriver.Chrome(options=option)
            # 指定调试地址
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver = driver_base

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


        if self._base_url != "":
            self.driver.get(self._base_url)

    #find_element方法私有
    def find(self,by,value):
        return self.driver.find_element(by=by,value=value)

    #find_elements方法私有
    def finds(self,by,value):
        return self.driver.find_elements(by=by,value=value)

    #quit方法私有
    def quit(self):
        self.driver.quit()

