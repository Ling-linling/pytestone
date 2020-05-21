import pytest
from case.common_function import jzrgg_api

@pytest.mark.web
@pytest.mark.webqyht
def test_get_industryinfosinglealllist_45(login_fix):
    '''获取所有行业的列表：基础数据，直接请求成功'''
    res = jzrgg_api(login_fix).get_industryinfosinglealllist()
    assert res["msg"] == "成功"
    assert res["code"] == 10000