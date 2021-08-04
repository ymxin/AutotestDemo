#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 12:49
# @Author  : yaomiaoxin
# @Email   : murcymurcy@163.com
# @File    : test_allure_login.py


import allure


@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login_success(self):
        print("登录成功用例")

    @allure.story("登录失败")
    def test_login_fail(self):
        print("登录失败用例")
        assert '1' == 1

    @allure.story("用户名输入错误")
    def test_login_fail_username(self):
        print("用户名缺失")

    @allure.story("密码输入错误")
    def test_login_fail_password(self):
        print("密码缺失")

    @allure.story("用户名和密码输入正确，登录成功")
    def test_success_username_and_password(self):
        with allure.step("点击用户名："):
            print("输入用户名")
        with allure.step("点击密码："):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录后登录成功~"):
            print("登录成功啦")


class TestLoginDemo:

    def test_login1(self):
        assert 1 != 2
