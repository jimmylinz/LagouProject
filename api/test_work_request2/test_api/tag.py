
from test_work_request2.test_api.baseapi import BaseApi


class Tag(BaseApi):

#创建标签
    def tag_add(self,tagname,tagid,token):
        date = {
            "method":"post",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}",
            "params" : {
                "tagname": f"{tagname}",
                "tagid": tagid
            }
        }
        re = self.send_api(date)
        return re

#更新标签名字
    def tag_updatename(self,tagname,tagid,token):
        date = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}",
            "params": {
                "tagname": f"{tagname}",
                "tagid": tagid
            }
        }
        re = self.send_api(date)
        return re

#删除标签
    def tag_delete(self,tagid,token):
        date = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}",
            "params": {
                "tagid": tagid
            }
        }
        re = self.send_api(date)
        return re

#获取标签成员
    def tag_get_person(self,tagid,token):
        date = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={token}",
            "params": {
                "tagid": tagid
            }
        }
        re = self.send_api(date)
        return re

#获取标签成员列表
    def tag_get_taglist(self,token):
        date = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}",
        }
        re = self.send_api(date)
        return re