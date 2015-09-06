#!/usr/bin/env python
# coding=utf-8
"""
合成音乐，执行python synmusic.py 123
来源：Numpy攻略
"""

import scipy.io.wavfile
import numpy
import sys
import matplotlib.pyplot

RATE = 44100
DTYPE = numpy.int16

#正弦波
def generate(freq, amp, duration, phi):
    t = numpy.linspace(0, duration, duration * RATE)
    data = numpy.sin(2 * numpy.pi * freq * t + phi) * amp

    return data.astype(DTYPE)

if len(sys.argv) != 2:
    print "Please input the number of tones to generate"
    sys.exit()

#初始化
NTONES = int(sys.argv[1])
amps = 2000. * numpy.random.random((NTONES,)) + 200.
durations = 0.19 * numpy.random.random((NTONES,)) + 0.01
keys = numpy.random.random_integers(1, 88, NTONES)
freqs = 440.0 * 2 ** ((keys - 49.)/12.)
phi = 2 * numpy.pi * numpy.random.random((NTONES))

tone = numpy.array([], dtype=DTYPE)

#谱曲
for i in xrange(NTONES):
    newtone = generate(freqs[i], amp=amps[i], duration=durations[i], phi=phi[i])
    tone = numpy.concatenate((tone, newtone))

scipy.io.wavfile.write('generated_tone.wav', RATE, tone)

#绘图
matplotlib.pyplot.plot(numpy.linspace(0, len(tone)/RATE, len(tone)), tone)
matplotlib.pyplot.show()
