#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 9:51
# @Author  : yaomiaoxin
# @Email   : murcymurcy@163.com
# @File    : test_calc.py
import pytest

from python_code.calc import Calculator


class TestCalc:

    def test_add(self):
        calc = Calculator()
        assert calc.add(1, 2) == 3

    # 断言异常
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError) as e:
            1 / 0
        # 断言异常类型 type
        assert e.type == ZeroDivisionError
        # 断言异常类型 value
        assert "division by zero" in str(e.value)

    @pytest.mark.xfail(raises=ZeroDivisionError)
    def test_f(self):
        1 / 0
