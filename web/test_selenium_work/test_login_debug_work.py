from selenium import webdriver

from selenium.webdriver.chrome.options import Options

class TestLogin:


    def test_login_debug(self):
        #实例化option
        option = Options()
        #需要和启动命令的端口号一致
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        #指定调试地址
        driver.get("https://work.weixin.qq.com/wework_admin/frame#apps")






