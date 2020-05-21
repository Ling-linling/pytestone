# import pytest
# # test_data = [
# #     ["M", {"message": "update some data!", "code": 0}],
# #     ["F", {"message": "update some data!", "code": 0}],
# #     ["x", {"message": "参数类型错误", "code": 3333}],
# #     ]
# from common.read_yml import readyml
# import os
#
# # 绝对路径
# curPath = os.path.dirname(os.path.realpath(__file__))
# print(curPath)
# yamPath = os.path.join(curPath, "test_data.yml")
# print(yamPath)
# test_data = readyml(yamPath)['updata_info']
# print(test_data)
#
#
# # @pytest.mark.skip("阻塞BUG")
# @pytest.mark.app
# @pytest.mark.appapi
# @pytest.mark.parametrize("test_input, expect", test_data)
# def test_updata_info_297(login_fix, test_input, expect):
#     '''修改个人信息'''
#     s = login_fix
#     url = "http://49.235.92.12:9000/api/v1/userinfo"
#     body = {"name": "test",
#             "sex": test_input,
#             "age": 20,
#             "mail": "283340479@qq.com"}
#     r = s.post(url, json=body)
#     print(r.text)
#     assert r.json()["message"] == expect["message"]
#     assert r.json()["code"] == expect["code"]
#
#
# @pytest.mark.web
# def test_updata_info_32(login_fix):
#     '''修改个人信息'''
#     s = login_fix
#     url = "http://49.235.92.12:9000/api/v1/userinfo"
#     body = {"name": "test",
#             "sex": "M",
#             "age": 20,
#             "mail": "283340479@qq.com"}
#     r = s.post(url, json=body)
#     print(r.text)
#     assert r.json()["message"] == "update some data!"
#     assert r.json()["code"] == 0
#     assert r.json()["data"]["mail"] == "283340479@qq.com"
#
# if __name__ == '__main__':
#     pytest.main(["-s", "test_update_info.py", "-m=app"])