#!/usr/bin/env python
# coding=utf-8

#应用k近邻算法改进约会网站配对效果
#来自：《机器学习实践》

import numpy
import operator

class Knn(object):
    def creat_dataset(self):
        group = numpy.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])    #作为已经训练的数组
        labels = ["A", 'A', 'B', 'B']                                      #上述数组坐标的标签
        return group, labels

    def knn_classify(self, testx, trainx, labels, k):
        trainx_size = trainx.shape[0]                                      #得到训练数组的大小
        diff_mat = numpy.tile(testx, (trainx_size, 1)) - trainx            #将归类对象数组矩阵扩展到和训练数组一致，然后做对应项的减法
        square_diff_mat = diff_mat ** 2                                   #计算每项的差的平方
        square_distances = square_diff_mat.sum(axis=1)                    #差的平方组成了矩阵，求矩阵行的各项和(axis=1),即对应项差的平方和
        distances = square_distances ** 0.5                               #将平方和开放
        sorted_distance_index = distances.argsort()                             #将各点得到的距离进行排序,注意：argsort返回的使对象的索引，并且按照值从小到大 
        #sorted_distance_index = numpy.argsort(distances)

        class_count = {}
        for i in range(k):                                                #根据设定的k值，从距离的最小到最大选k个
            ith_label = labels[sorted_distance_index[i]]
            class_count[ith_label] = class_count.get(ith_label, 0) + 1    #记录labels中的标签的出现次数
        
        sorted_class_count = sorted(class_count.iteritems(), key = operator.itemgetter(1), reverse = True)  #对字典键值按照值排序，从大到小，选择出现频率最高的返回
        return sorted_class_count[0][0]

    def file2matrix(self, filename):
        """
        将文本记录转换为矩阵，并输出，还输出一个类标签向量
        """
        fr = open(filename)
        array_lines = fr.readlines()
        number_lines = len(array_lines)
        return_mat = numpy.zeros((number_lines, 3))
        class_label_vector = []
        index = 0
        for line in array_lines:
            line = line.strip()
            list_from_line = line.split(',')
            return_mat[index,:] = list_from_line[0:3]
            class_label_vector.append(int(list_from_line[-1]))
            index += 1
        return return_mat, class_label_vector

k = Knn()
groups, labels = k.creat_dataset()
result = k.knn_classify([0, 0], groups, labels, 3)
print result
mat, ls = k.file2matrix("test.txt")
print mat
print ls
