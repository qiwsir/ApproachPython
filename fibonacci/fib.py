#!/usr/bin/env python
# coding=utf-8

"""
    Fibonacci数列中的每一项都是该项之前的两项和。如：1,1,2,3,5,8,13...
    以下的计算方法采用了维基百科（https://zh.wikipedia.org/zh-sg/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0%E5%88%97）中的“初等代数解法”
"""

import numpy

#计算黄金比例

phi = (1 + numpy.sqrt(5)) / 2
print 'Phi', phi

#当某项取值不大于2百万，则最大索引值，计算方法是将前述维基百科中计算某项值的公式，赋予该项值为200万，计算索引值n
#因为需要把对数的底数进行转化，所以使用对数函数log
#不需要对计算结果向下取整，因为在arange()中传入参数的时候自动完成取整操作

maxn = numpy.log(2 * 10 ** 6 * numpy.sqrt(5) + 0.5) / numpy.log(phi)
print maxn

#得到最大值的项小于上述值（200万）的索引列表
#maxn本来值不是整数，但在numpy.arange()中自动向下取整，例如：
#>>> numpy.arange(1, 9.8)
#array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9. ])

n = numpy.arange(1, maxn)
print n

#根据前述维基百科中给出的fibonacci数列公式，计算没一项的值
#注意这里的n是array()对象,不是list。从而实现了循环

fib = (phi ** n - (-1 / phi) ** n) / numpy.sqrt(5)
print "First 9 Fibonacci Numbers", fib[:9]

#将上述结果转化为整数。

fib = fib.astype(int)
print "Integers", fib


