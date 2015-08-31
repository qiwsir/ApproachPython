#!/usr/bin/env python
# coding=utf-8
"""
来自《numpy功略》p45
寻找某个数字的最大质因数使多少.
"""
import numpy

N = 600851475143
LIM = 10 ** 6

def factor(n):
    #创建尝试值数组
    a = numpy.ceil(numpy.sqrt(n))
    lim = min(n, LIM)
    a = numpy.arange(a, a + lim)
    b2 = a ** 2 - n

    #检查数组b2中的元素是否使某个整数的平方
    fractions = numpy.modf(numpy.sqrt(b2))[0]

    #检查小数部分为0的数组元素
    indices = numpy.where(fractions == 0)

    #找到第一个小数部分为0的数组元素
    a = numpy.ravel(numpy.take(a, indices))[0]
    a = int(a)
    b = numpy.sqrt(a ** 2 - n)
    b = int(b)
    c = a + b
    d = a - b

    if c == 1 or d == 1:
        return

    print c, d
    factor(c)
    factor(d)

factor(N)
