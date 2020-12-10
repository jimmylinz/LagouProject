import pytest

from test_work_request2.test_api.tag import Tag
from test_work_request2.test_api.wework import Wework


class TestTag(Wework):
    @pytest.fixture(scope="session")
    def token(self,get_token):
        return get_token

    def setup(self):
        self.tag = Tag()

    def create_muti_data(self):
        data = [("tag%0d"% x,"1001" + str(x)) for x in range(10)]
        return data

    @pytest.mark.parametrize("tagname,tagid",create_muti_data("xxx"))
    def test_all(self,tagname,tagid,get_token):
        try:
            assert "created" == self.tag.tag_add(tagname,tagid,get_token)['errmsg']
        except AssertionError as e:
            if "UserTag Name Already Exist" in e.__str__():
                res = self.tag.tag_delete(get_token,tagid)
                self.tag.tag_get_person(res,get_token)
                self.tag.tag_get_person(res,get_token)
            if "invalid tagid" in e.__str__():
                self.tag.tag_delete(tagid,get_token)
            assert self.tag.tag_add(tagname,tagid,get_token)['errmsg'] == "created"

        assert self.tag.tag_get_person(tagid,get_token)['errmsg'] == "ok"

        assert self.tag.tag_delete(tagid,get_token)['errmsg'] == "delete"

        assert self.tag.tag_updatename(1,2,get_token)['errmsg'] == "updated"












