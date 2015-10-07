#!/usr/bin/env python
# coding=utf-8

#朴素贝叶斯算法一个例子
#高斯分布
#来源：http://python.jobbole.com/81019

import csv
import random
import math


def loadCsv(filename):
    """
    加载数据文件，因为加载的使CSV格式文件，它没有标题行和任何引号，利用此函数，将它转化为数字组成的列表，并返回。
    """
    lines = csv.reader(open(filename, "rb"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

def splitDataset(dataset, split_ratio):
    """
    将数据按照一定比例分为两部分，一部分使训练集合，另外一部分使测试集。
    """
    train_size = int(len(dataset) * split_ratio)    #训练集合的长度
    train_set = []                                 #训练集合数据存放
    copy = list(dataset)
    while (len(train_set) < train_size):
        index = random.randrange(len(copy))        #在copy中随机取一个索引，然后把该索引值加入到训练集合中。训练集合长度不大于train_size值。每取出一个，就将该值删除，所以用pop，删除同时返回删除值。
        train_set.append(copy.pop(index))
    return (train_set, copy)               #返回训练集和测试集合两个数据

def separateByClass(dataset):
    """
    将训练集中的数据分组
    """
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):     #以每个列表的最后一个元素为特征(key)，同样的化为一个键下的值。
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

def mean(numbers):
    """
    计算每个类中每个属性的平均值，它作为高斯分布的中值。
    """
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    """
    再计算每个类中每个属性的标准差，标准差使方差的平方根。方差使每个属性值与平均值的离差平方的平均数，这里是用N-1方法，也就是在计算方差的时候，属性值的个数减1
    """
    avg = mean(numbers)
    variance = sum([pow(x-avg, 2) for x in numbers]) / float(len(numbers)-1)
    return math.sqrt(variance)

def summarize(dataset):
    """
    计算每个属性的平均值和标准差
    """
    summarizes = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]     #zip()函数的使用
    del summarizes[-1]     #最后一个作为KEY了，所以删除
    return summarizes

def summarizeByClass(dataset):
    """
    针对每个属性，生成相应的上述计算结果
    """
    separated = separateByClass(dataset)
    summaries = {}
    for class_value, instances in separated.iteritems():
        summaries[class_value] = summarize(instances)
    return summaries

def calculateProbability(x, mean, stdev):
    """
    计算某个值属于某个类的可能性，概率。即高斯概率密度函数
    """
    exponet = math.exp(-(math.pow(x-mean, 2) / (2*math.pow(stdev, 2))))
    return (1 / (math.sqrt(2*math.pi)*stdev)) * exponet

def calculateClassProbabilities(summaries, input_vector):
    """
    计算每个类别的概率，得到数据样本属于某个类的概率
    """
    probabilities = {}
    for class_value, class_summaries in summaries.iteritems():
        probabilities[class_value] = 1
        for i in range(len(class_summaries)):
            mean, stdev = class_summaries[i]
            x = input_vector[i]
            probabilities[class_value] *= calculateProbability(x, mean, stdev)
    return probabilities

def predict(summaries, input_vector):
    """
    单一预测，计算一个数据样本属于每个类的概率之后，找出其中的最大概率，并返回关联的类
    """
    probabilities = calculateClassProbabilities(summaries, input_vector)
    best_label, best_prob = None, -1
    for class_value, probability in probabilities.iteritems():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = class_value
    return best_label

def getPredictions(summaries, test_set):
    """
    多重预测，对测试数据中么个数据样本进行预测，并返回预测结果列表
    """
    predictions = []
    for i in range(len(test_set)):
        result = predict(summaries, test_set[i])
        predictions.append(result)
    return predictions

def getAccuracy(test_set, predictions):
    """
    检验预测结果的准确概率
    """
    correct = 0
    for x in range(len(test_set)):
        if test_set[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(test_set))) * 100.0

def main():
    filename = "pima.data.csv"
    split_ratio = 0.67
    dataset = loadCsv(filename)
    train, test = splitDataset(dataset, split_ratio)
    print 'Split {0} rows into train = {1} and test={2} rows'.format(len(dataset), len(train), len(test))

    summaries_main = summarizeByClass(train)

    predictions_main = getPredictions(summaries_main, test)
    accuracy = getAccuracy(test, predictions_main)
    print "Accuracy: {0}%".format(accuracy)

main()
