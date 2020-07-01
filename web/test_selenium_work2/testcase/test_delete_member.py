from web.test_selenium_work2.page.main_page import MainPage


class TestDeletemember():
    def setup(self):
        self.main = MainPage()

    def test_deletemember(self):
        assert self.main.goto_contact().delete_member() == None

    def teardown(self):
        self.main.quit()