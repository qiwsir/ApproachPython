#!/usr/bin/env python
# coding=utf-8

"""
使用python对文本分类，利用贝叶斯算法
来源：机器学习实践
"""
from numpy import *

def createVocabList(data_set):
    """
    生成词汇列表，即将一个由单词组成的矩阵转换为词汇没有重复的列表
    data_set是一个由词汇组成的列表，每个子元素也是一个列表。
    """
    vocab_set = set([])
    for document in data_set:
        vocab_set = vocab_set | set(document)     #集合合并，通过set(document)将每个列表中重复的词汇去掉
    return list(vocab_set)

def setOfWords2Vec(vocab_list, input_set):
    """
    将词汇列表根据向量特征进行转化，结果是从文本中构建词汇向量
    """
    return_vec = [0] * len(vocab_list)       #创建一个与词汇列表一样长度的都是0的向量（列表）
    for word in input_set:
        if word in vocab_list:               #如果词汇表中的单词在input_set中，则该词汇表向量值为1（1代表了侮辱文字）,否则就是原来的0
            return_vec[vocab_list.index(word)] = 1
        else:
            print "the word: {0} is not in my Vocabulary!".format(word)
    return return_vec

def bagOfWords2VecMN(vocab_list, input_set):
    return_vec = [0] * len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            return_vec[vocab_list.index(word)] += 1     #功能同前函数，只是这里修改，这是文档词袋模型。
        else:
            print "the word: {0} is not in my Vocabulary!".format(word)
    return return_vec

def trainNB0(train_matrix, train_category):
    """
    朴素贝叶斯分类器
    train_matrix:训练集合
    train_category:训练分类[0, 1, 0, 1, 0, 1],1 代表侮辱性文字， 0代表正常言论
    """
    num_train_docs = len(train_matrix)
    print num_train_docs
    num_words = len(train_matrix[0])
    p_abusive = sum(train_category) / float(num_train_docs)    #在训练分类中侮辱性文字占训练集合的概率
    #p0_num = zeros(num_words)      #正常文字初始概率
    #p1_num = zeros(num_words)      #侮辱性文字初始概率
    #为了避免出现概率值为0
    p0_num = ones(num_words)       #把初始值设为1
    p1_num = ones(num_words)
    #p0_denom = 0.0
    #p1_denom = 0.0
    p0_denom = 2       #将分母初始值设置为2
    p1_denom = 2
    for i in range(num_train_docs):    #分成两部分
        if train_category[i] == 1:
            p1_num += train_matrix[i]           #分子分别为各行所对应数值的和（最终结果为每列数值的和）
            p1_denom += sum(train_matrix[i])    #分母为所有数值的和
        else:
            p0_num += train_matrix[i]
            p0_denom += sum(train_matrix[i])
    #p1_vect = p1_num / p1_denom                 #最终得到每个词汇在全体词汇中所占比例
    #p0_vect = p0_num / p0_denom
    #为了避免太小的数值，对上面的值取对数
    p1_vect = log(p1_num / p1_denom)
    p0_vect = log(p0_num / p0_denom)
    return p0_vect, p1_vect, p_abusive

def classifyNB(vec2classify, p0vec, p1vec, pclass1):
    p1 = sum(vec2classify * p1vec) + log(pclass1)
    p0 = sum(vec2classify * p0vec) + log(1.0 - pclass1)
    if p1 > p0:
        return 1
    else:
        return 0

def main():
    data_set = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
               ['maybe','not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
               ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
               ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
               ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
               ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]

    class_vec = [0, 1, 0, 1, 0, 1]     #分类，对应data_set的行数

    vocab_list = createVocabList(data_set)
    train_mat = []
    for listindata in data_set:
        train_mat.append(setOfWords2Vec(vocab_list, listindata))    #以vocab_list为标准，如果listindata里的词汇在vocab_list中则为1,最终得到一个训练集合train_mat，这个矩阵的每一行都记录了data_set中所有词汇在vocab_list中出现次数，出现了就是1
    p0v,p1v,pab = trainNB0(array(train_mat), array(class_vec))

    test_entry = ['love', 'my', 'dalmation']
    this_doc = array(setOfWords2Vec(vocab_list, test_entry))
    print test_entry, 'classified as:', classifyNB(this_doc, p0v, p1v,pab)

    
main()
