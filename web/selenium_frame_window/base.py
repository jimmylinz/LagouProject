import os

from selenium import webdriver


class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS
        elif browser == 'safari':
            self.driver = webdriver.Safari
        else:
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()