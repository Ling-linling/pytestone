# 公共的操作函数
from case.apijzr.jzrqyht_class import JzrqyhtAPi
from case.apijzr.jzrgg_class import JzrggAPi
def login(s):
    '''登录获取token'''
    # s = requests.session()  # 会话  代码里面的浏览器，模拟浏览器的功能
    url = "http://114.115.153.29:9000/api/CompanyUser/CompanyUserLogin"
    body = {
        "Account": "15812345678",
        "Pwd": "123456"
    }

    # 转json
    r = s.post(url, json=body)
    # print(r.json())

    # token
    token = r.json()["data"]["Token"]
    print("取出Token:%s" % token)

    h = {
        "Token": "%s" % token
    }
    s.headers.update(h)  # 更新到session会话
    # 更新之后的头部
    # print(s.headers)
    return token

def jzrqyht_api(s):
    '''实例化--建筑人企业后台方法'''
    return JzrqyhtAPi(s)

def jzrgg_api(s):
    '''实例化--建筑人公共方法'''
    return JzrggAPi(s)

from common.read_yml import readyml
import os
def get_testdata(curPath, testdata):
    ymlPath = os.path.join(curPath, "test_data.yml")
    test_data = readyml(ymlPath)[testdata]
    return test_data