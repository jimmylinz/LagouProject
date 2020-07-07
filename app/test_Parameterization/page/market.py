from app.test_Parameterization.page.base_page import BasePage
from app.test_Parameterization.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yml")
        return Search(self._driver)