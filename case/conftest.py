import pytest
import requests
from case.common_function import login

@pytest.fixture(scope="module")
def login_fix():
    '''自定义一个前置的操作'''
    print("先登陆")
    s = requests.session()
    login(s)
    return s

@pytest.fixture(scope="function")
def unlogin_fix():
    '''自定义一个前置的操作'''
    print("不登陆")
    s = requests.session()
    s.headers.update({"Token": "/7ath6z0TMZheDLipnoj7yZc2BdUAgpiqqm19q3JCJVrKKDvZAhFwuSxPLN6a5ieJK6U08jG8k8x="})
    return s