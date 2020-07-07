from appium import webdriver

desire_caps = {}
desire_caps['platformName'] = 'android'
desire_caps['platformVersion'] = '6.0'
desire_caps['deviceName'] = 'emulator-5554'
desire_caps['appPackage'] = 'com.xueqiu.android'
desire_caps['appActivity'] = '.view.WelcomeActivityAlias'
desire_caps['noReset'] = 'true'
desire_caps['dontStopAppOnReset'] = 'true'
desire_caps['skipDeviceInitialization'] = 'true'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_caps)
driver.implicitly_wait(5)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.back()
driver.back()
driver.quit()