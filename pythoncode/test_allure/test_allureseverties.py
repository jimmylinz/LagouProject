import allure
import pytest


@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial():
    pass

@allure.severity(allure.severity_level.MINOR)
def test_with_minor():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal():
    pass

@allure.severity(allure.severity_level.CRITICAL)
class TestAllureSeverities():
    
    def test_with_critical(self):
        pass

    @allure.severity(allure.severity_level.BLOCKER)
    def test_with_blocker(self):
        pass

if __name__ == '__main__':
    pytest.main()