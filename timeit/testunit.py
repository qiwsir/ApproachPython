#!/usr/bin/env python
# coding=utf-8

#timeit使python标准库中一个用来测试代码段执行时间的模块。
#本例中将使用它来测量不同数组sort的时间

import numpy
import timeit
import matplotlib.pyplot

intergers = []

def dosort():
    intergers.sort()

def measure():
    timer = timeit.Timer('dosort()', 'from __main__ import dosort')
    return timer.timeit(10 ** 2)

powersOf2 = numpy.arange(0, 19)
sizes = 2 ** powersOf2

times = numpy.array([])

for size in sizes:
    intergers = numpy.random.random_integers(1, 10 ** 6, size)
    times = numpy.append(times, measure())

fit = numpy.polyfit(sizes * powersOf2, times, 1)
print fit

matplotlib.pyplot.title("Sort array sizes vs execution times.")
matplotlib.pyplot.xlabel("Size")
matplotlib.pyplot.ylabel("(s)")
matplotlib.pyplot.semilogx(sizes, times, "ro")
matplotlib.pyplot.semilogx(sizes, numpy.polyval(fit, sizes * powersOf2))
matplotlib.pyplot.show()
