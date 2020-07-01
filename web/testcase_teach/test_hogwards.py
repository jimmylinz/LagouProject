from time import sleep

from selenium import webdriver


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://ceshiren.com/")

        self.driver.find_element_by_link_text("所有分类").click()
        
        self.driver.find_elements_by_css_selector("#ember162 .category-name").click()
