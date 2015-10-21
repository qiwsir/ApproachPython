#!/usr/bin/env python
# coding=utf-8
"""
logistic回归
"""
import numpy

def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def sigmoid(inX):
    return 1.0 / (1 + numpy.exp(-inX))

def gradAscent(dataMatIn, classLabels):
    """
    实现梯度上升算法
    """
    dataMatrix = numpy.mat(dataMatIn)
    labelMat = numpy.mat(classLabels).transpose()
    m, n = numpy.shape(dataMatrix)     #返回矩阵的行列，m是行，n是列
    alpha = 0.001
    maxCycles = 500
    weights = numpy.ones((n, 1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = (labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights

dataArr, labelMat = loadDataSet()
w = gradAscent(dataArr, labelMat)
print w
