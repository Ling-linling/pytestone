import os

from case.common_function import jzrqyht_api
import pytest
import requests
# from common.read_yml import readyml
# curPath = os.path.dirname(os.path.realpath(__file__))
# ymlPath = os.path.join(curPath, "test_data.yml")
# test_data = readyml(ymlPath)['get_enterpriseinfodetail']
from case.common_function import get_testdata
curPath = os.path.dirname(os.path.realpath(__file__))
test_data=get_testdata(curPath=curPath, testdata='get_enterpriseinfodetail')
@pytest.mark.web
@pytest.mark.webqyht
def test_get_enterpriseinfodetail_38(login_fix, enterpriseId=4):
    '''查询企业中心的用户信息：头部传用户登录Token，可以查询企业用户信息'''
    res = jzrqyht_api(login_fix).get_enterpriseinfodetail(enterpriseId)
    assert res["msg"] == "成功"
    assert res["code"] == 10000

@pytest.mark.web
@pytest.mark.webqyht
def test_get_enterpriseinfodetail_39(enterpriseId=4):
    '''查询企业中心的用户信息：头部不传Token，提示登录失效'''
    s = requests.session()
    res = jzrqyht_api(s).get_enterpriseinfodetail(enterpriseId)
    assert res["msg"] == "登录失效,请重新登录"
    assert res["code"] == 10005

@pytest.mark.web
@pytest.mark.webqyht
def test_get_enterpriseinfodetail_40(unlogin_fix, enterpriseId=4):
    '''查询企业中心的用户信息：头部传错误或失效的Token，提示登录失效'''
    # s = requests.session()
    # s.headers.update({"Authorization": "Token f4b9a1dffbf525ecc93f8c80035c60fa546d5xxx"})
    res = jzrqyht_api(unlogin_fix).get_enterpriseinfodetail(enterpriseId)
    assert res["msg"] == "登录失效,请重新登录"
    assert res["code"] == 10005

# @pytest.mark.web
# @pytest.mark.webqyht
# def test_get_enterpriseinfodetail_41(unlogin_fix,enterpriseId=None):
#     '''查询企业中心的用户信息：params不传enterpriseId，无法查询到企业详情'''
#     res = jzrqyht_api(unlogin_fix).get_enterpriseinfodetail(enterpriseId)
#     assert res["Message"] == "找不到与请求 URI“http://114.115.153.29:9000/api/EnterpriseInfo/GetEnterpriseInfoDetail”匹配的 HTTP 资源。"
#     assert res["MessageDetail"] == "在控制器“EnterpriseInfo”上找不到与该请求匹配的操作。"

@pytest.mark.web
@pytest.mark.webqyht
@pytest.mark.parametrize("test_input, expect", test_data)
def test_get_enterpriseinfodetail_42(login_fix, test_input, expect):
    '''查询企业中心的用户信息：params传不存在、非整型、特殊字符、中文的enterpriseId，无法查询到企业详情'''
    res = jzrqyht_api(login_fix).get_enterpriseinfodetail(enterpriseId=test_input)
    if expect.get("Message") != None:
        assert res["Message"] == expect["Message"]
        assert res["MessageDetail"] == expect["MessageDetail"]
    else:
        assert res["msg"] == expect["msg"]
        assert res["code"] == expect["code"]

@pytest.mark.web
@pytest.mark.webqyht
def test_get_enterpriseinfodetail_43(login_fix, enterpriseId=2147483647):
    '''查询企业中心的用户信息：params传2147483647大小的enterpriseId，可以查询到企业详情'''
    res = jzrqyht_api(login_fix).get_enterpriseinfodetail(enterpriseId)
    assert res["msg"] == "成功"
    assert res["code"] == 10000

def test_get_enterpriseinfodetail_44(login_fix, enterpriseId=2147483648):
    '''查询企业中心的用户信息：params传2147483648大小的enterpriseId，可以查询到企业详情'''
    res = jzrqyht_api(login_fix).get_enterpriseinfodetail(enterpriseId)
    assert res["Message"] == "请求无效。"
    assert res["MessageDetail"] == "对于“JZRZPWebAPI.Controllers.Company.EnterpriseInfoController”中方法“JZR.Model.PublicModel`1[JZRZP.Model.EnterpriseInfoReturn] GetEnterpriseInfoDetail(Int32)”的不可以为 null 的类型“System.Int32”的参数“enterpriseId”，参数字典包含一个 null 项。可选参数必须为引用类型、可以为 null 的类型或声明为可选参数。"