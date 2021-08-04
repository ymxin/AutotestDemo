#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/25 11:42
# @Author  : yaomiaoxin
# @Email   : murcymurcy@163.com
# @File    : test_demo.py

def f():
    return 3

def test_function():
    a = f()
    assert a % 2 == 0, f'判断a为偶数，当前a的值为：{a}'