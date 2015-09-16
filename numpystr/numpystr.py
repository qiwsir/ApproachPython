#!/usr/bin/env python
# coding=utf-8

#numpy的chararray对象，专门存放字符串。优点：用索引获取数组元素时，字符串中多余的空格会自动删除；做比较运算时，字符串后端的空格会自动删除；支持向量化的字符串操作，不需要使用循环语句

import urllib2
import numpy
import re

response = urllib2.urlopen("http://www.itdiffer.com")
html = response.read()
html = re.sub(r'<.*?>', '', html)
carray = numpy.array(html).view(numpy.chararray)
carray = carray.expandtabs(1)     #把tab字符替换为空格，参数为空格数
carray = carray.splitlines()      #按行分割字符串

print carray
