#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 15:34
# @Author  : yaomiaoxin
# @Email   : murcymurcy@163.com
# @File    : test_login.py
import pytest

@pytest.fixture()
def login():
    print("登录操作")
    yield
    print("注销操作")

@pytest.fixture()
def login3():
    print("登录操作3")
    yield
    print("注销操作3")


def test_one(login):
    print("用例one，执行前先登录")


def test_two():
    print("用例two，无需登录")

# 可以叠加多个 @pytest.mark.usefixtures() ，先执行的放底层，后执行的放上层
@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("login3")
def test_three():
    print("用例three，执行前先登录")

# 设置autouse=True 所有测试用例都会执行登录操作
# @pytest.fixture(autouse=True)
def login2():
    print("登录操作2")
#
# def test_four():
#     print("用例4，执行前先登录2")

# 在类声明上面加 @pytest.mark.usefixtures() ，
# 代表这个类里面所有测试用例都会调用该fixture
@pytest.mark.usefixtures("login")
class TestDemo:

    def test_five(self):
        print("用例5 需要登录操作")

    def test_six(self):
        print("用例6 需要登录操作")
