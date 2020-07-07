from app.test_Parameterization.page.base_page import BasePage
from app.test_Parameterization.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yml")
        return Market(self._driver)