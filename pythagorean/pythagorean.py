#!/usr/bin/env python
# coding=utf-8

import numpy
import numpy.testing

#三个自然数a,b,c,(假设a<b<c)，且a^2 + b^2 = c^2，则这三个数被称为勾股数

#本例要寻找三个勾股数的和为1000的时候，这三个数分别是什么？

m = numpy.arange(33)
n = numpy.arange(33)

#计算a,b,c
a = numpy.subtract.outer(m ** 2, n ** 2)     #a = m^2 - n^2
b = 2 * numpy.multiply.outer(m, n)           #b = 2mn
c = numpy.add.outer(m ** 2, n ** 2)          #c = m^2 + n^2

#找到符合条件的索引a+b+c = 1000
idx = numpy.where((a + b + c) == 1000)

#检查结果
numpy.testing.assert_equal(a[idx] ** 2 + b[idx] ** 2, c[idx] ** 2)
print a[idx],  b[idx], c[idx]
