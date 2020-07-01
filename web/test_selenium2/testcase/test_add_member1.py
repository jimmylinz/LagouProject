from web.test_selenium2.page.main_page1 import MainPage


class TestAddMember():

    def setup(self):
        self.main = MainPage()

    def test_add_member(self):
        assert "东巴1" in self.main.goto_add_member().add_member().get_member()

    def test_add_member_fail(self):
        assert "东巴2" not in self.main.goto_add_member().add_member_fail().get_member()

    def teardown(self):
        self.main.quit()