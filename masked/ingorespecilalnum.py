#!/usr/bin/env python
# coding=utf-8

#忽略负值和极大或者极小值
#来源：NUMPY攻略

import numpy
import pandas.io.data
import sys
import matplotlib.pyplot

def get_close(ticker):
    quotes = pandas.io.data.DataReader(ticker, "yahoo", start="2014/9/17")    #从雅虎财经上获得某股票的数据
    return numpy.array([q for q in quotes['Close']])                #返回某数据（收盘价)

close = get_close("BABA")           #得到阿里巴巴的股价

triples = numpy.arange(0, len(close), 3)       #创建一个数组，数组的元素使从0到len(close)中能够被3整除的数
print "Triples", triples[:10]                  #打印前十个看看

signs = numpy.ones(len(close))
print "Signs", signs[:10]
signs[triples] = -1                  
print "Signs", signs[:10]

ma_log = numpy.ma.log(close * signs)         #close*signs 制造出数组中某些股价数据使负数（被3整除的项股价变成了负数),对该数组中每个数计算对数
print "Masked logs", ma_log[:10]

dev = close.std()       #得到标准差
avg = close.mean()      #得到平均数
inside = numpy.ma.masked_outside(close, avg - dev, avg + dev)     #比平均数大或者小一个标准差的数，列为极值。只要在这个范围以内的数值
print "Inside", inside[:10]

matplotlib.pyplot.subplot(311)
matplotlib.pyplot.title("Original")
matplotlib.pyplot.plot(close)

matplotlib.pyplot.subplot(312)
matplotlib.pyplot.title("Log Masked")
matplotlib.pyplot.plot(numpy.exp(ma_log))

matplotlib.pyplot.subplot(313)
matplotlib.pyplot.title("Not Extreme")
matplotlib.pyplot.plot(inside)

matplotlib.pyplot.show()
