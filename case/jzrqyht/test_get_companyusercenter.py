from case.common_function import jzrqyht_api
import pytest
import allure

@allure.step("步骤1：点击雇主品牌")
def step_1():
    print("点击雇主品牌")

@allure.feature("查看企业中心的用户信息页面")
class TestGetCompanyUserCenterPage():
    '''查看企业中心的用户信息页面'''

    @allure.story("查询企业中心的用户信息的用例")
    @allure.testcase("http://106.54.216.39:8088/zentao/testcase-view-36-2.html")
    def test_get_companyusercenter_36(self, login_fix):
        '''【用例描述】：查询企业中心的用户信息：头部传用户登录Token，可以查询企业用户信息
        【前置条件】：用户先登录
        【step1】：点击雇主品牌
        【step2】：查看企业中心用户信息 -> 可以查询企业用户信息'''
        step_1()
        res = jzrqyht_api(login_fix).get_companyusercenter()
        assert res["msg"] == "成功"
        assert res["code"] == 10000

    @allure.story("无法查询企业中心的用户信息的用例")
    @allure.testcase("http://106.54.216.39:8088/zentao/testcase-view-37-0-testcase-0.html")
    def test_get_companyusercenter_37(self, unlogin_fix):
        '''【用例描述】：查询企业中心的用户信息：头部传错误或失效的Token，提示登录失效
        【前置条件】：头部传错误或失效的Token
        【step1】：点击雇主品牌
        【step2】：查看企业中心用户信息 -> 提示登录失效'''
        # s = requests.session()
        # s.headers.update({"Authorization": "Token f4b9a1dffbf525ecc93f8c80035c60fa546d5xxx"})
        step_1()
        res = jzrqyht_api(unlogin_fix).get_companyusercenter()
        assert res["msg"] == "登录失效,请重新登录"
        assert res["code"] == 10005
