import pytest
import os
from case.common_function import jzrgg_api
from case.common_function import get_testdata

# curPath = os.path.dirname(os.path.realpath(__file__))
# test_data=get_testdata(curPath=curPath, testdata='newgetbykey')
# @pytest.mark.web
# @pytest.mark.webqyht
# @pytest.mark.parametrize("test_input, expect", test_data)
# def test_newgetbykey_46(login_fix, test_input, expect):
#     '''获取key值下的数据：头部传不正确的Content-Type，body传正确的key，提示资源不支持请求类型'''
#     res = jzrgg_api(login_fix).newgetbykey()


@pytest.mark.web
@pytest.mark.webqyht
def test_newgetbykey_47(login_fix):
    '''获取key值下的数据：头部传正确的Content-Type，body传正确的key，请求成功'''
    res = jzrgg_api(login_fix).newgetbykey()
    assert res["msg"] == "成功"
    assert res["code"] == 10000