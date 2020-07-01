import allure

@allure.link("http://www.baidu.com",name="百度链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass

TEST_CASE_LINK = 'https://www.baidu.com'
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_testcase_link():
    print("这是一条测试用例的链接，连接到测试")
    pass

# --allure-link-pattern=issue:https://www.baidu.com/issue/{}
@allure.issue('140','这是一个issue')
def test_with_issue_link():
    pass