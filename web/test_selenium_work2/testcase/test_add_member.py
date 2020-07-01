from web.test_selenium_work2.page.main_page import MainPage

class TestAddmember():
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        assert "绝对4" in self.main.goto_add_member().add_member().get_addmember()

    def test_addmember_fail(self):
        assert "绝对2" not in self.main.goto_add_member().add_member_fail().get_addmember()

    def teardown(self):
        self.main.quit()

