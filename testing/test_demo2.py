#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 14:05
# @Author  : yaomiaoxin
# @Email   : murcymurcy@163.com
# @File    : test_demo2.py

def setup_module():
    print('开始  module')


def teardown_module():
    print('结束 module')


def setup_function():
    print('开始 function')


def teardown_function():
    print('结束 function')


def test_one():
    print('这是one')


class TestDemo:

    def setup_class(self):
        print('开始 class')

    def teardown_class(self):
        print('结束 class')

    def setup_method(self):
        print('开始 method')

    def teardown_method(self):
        print('结束 method')

    def setup(self):
        print('开始 setup')

    def teardown(self):
        print('结束 setup')

    def test_two(self):
        print('这是two')
        assert 1 == 1

    def test_three(self):
        print('这是three')
        assert 1 > 0



# test_demo2.py
# 开始  module
# 开始 function
# 这是one
# .结束 function
# 开始 class
# 开始 method
# 开始 setup
# 这是two
# .结束 setup
# 结束 method
# 开始 method
# 开始 setup
# 这是three
# .结束 setup
# 结束 method
# 结束 class
# 结束 module
