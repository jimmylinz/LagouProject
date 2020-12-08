import pytest

from api.test_work_request2.test_api.tag import Tag
from api.test_work_request2.test_api.wework import Wework


class TestAll:
    @pytest.fixture(scope="session")
    def token(self):
        wework = Wework()
        yield wework.get_token()

    def setup(self):
        self.tag = Tag()
    
    def test_tag_add(self,token):
        re = self.tag.tag_add("AC",13,token)
        print(re)
        # assert re['tagid'] == "12"

    def test_tag_updatename(self):
        re = self.tag.tag_updatename("AC",12)
        assert re['errmsg'] == "updated"
    
    def test_tag_delete(self):
        re = self.tag.tag_delete(12)
        assert re['errmsg'] == "deleted"
    
    def test_tag_get_person(self):
        re = self.tag.tag_get_person(12)
        assert re['errmsg'] == "ok"

