from web.test_pageobject.page.main import Main


class TestRegiester:
    def setup(self):
        self.main = Main()

    def test_regiester(self):
        assert self.main.goto_login().login_regiester().regiester()