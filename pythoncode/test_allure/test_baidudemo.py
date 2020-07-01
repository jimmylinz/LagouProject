import allure
import time
import pytest
from selenium import webdriver

@allure.testcase("https://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_date",["allure","pytest","unittest"])
def test_step_demo(test_date):

    with allure.step("打开百度"):
        driver = webdriver.Chrome("E:\python\Scripts\chromedriver.exe")
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step("输入搜索词"):
        driver.find_element_by_id("kw").send_keys(test_date)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./photo/a.png")
        allure.attach.file("./photo/a.png",attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()