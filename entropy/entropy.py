#!/usr/bin/env python
# coding=utf-8

#参考：机器学习实践
#以下计算中，数据集的特征是：（1）由列表元素构成，且所有列表元素长度一致；（2）列表的最后一个元素是该列表的类别标签；

from math import log

def cal_shannon_ent(dataset):
    """
    计算指定数据集的熵
    """
    num_entries = len(dataset)
    label_counts = {}
    for featvec in dataset:
        current_label = featvec[-1]       #数据集dataset的最后一项使该数据的特征，例如：[[1,1,'yes'], [1,0,'no']]
        if current_label not in label_counts.keys():  #以特征为键，建立字典，记录每个特征的出现次数
            label_counts[current_label] = 0
        label_counts[current_label] += 1

    shannon_ent = 0       #熵的默认值
    for key in label_counts:
        prob = float(label_counts[key]) / num_entries
        shannon_ent -= prob * log(prob, 2)     #以2为底求对数

    return shannon_ent

def split_data_set(dataset, index, value):
    """
    按照指定的数据特征，划分数据集。index使数据集中的数据位置，value使该数据值
    [1,0,'no'], index=0,即第一个,value=1，即要第一个使1的数据集。也就是以哪个数据为划分依据.
    """
    ret_data_set = []
    for featvec in dataset:
        if featvec[index] == value:
            reduced_featvec = featvec[:index]
            reduced_featvec.extend(featvec[index+1:])
            ret_data_set.append(reduced_featvec)
    return ret_data_set

def choose_best_feature_split(dataset):
    """
    选择最好的数据集划分方式。也就是找到以哪一个index划分，才能得到最好的分类结果。好的标准是符合熵最小。
    """
    num_features = len(dataset[0]) - 1     #得到除了最后的类别标签之外的特征值个数
    base_entropy = cal_shannon_ent(dataset)   #计算数据集的熵
    best_info_gain = 0
    best_feature = -1
    for i in range(num_features):
        feat_list = [example[i] for example in dataset]    #将数据集的列的值取出来
        unique_values = set(feat_list)                     #得到不重复的值
        new_entropy = 0.0
        for value in unique_values:
            sub_dataset = split_data_set(dataset, i, value)
            prob = len(sub_dataset) / float(len(dataset))
            new_entropy += prob * cal_shannon_ent(sub_dataset)
        info_gain = base_entropy - new_entropy       #将原有的熵和新计算的熵对比，如果大于零，则新的熵减小了，熵小，则向有序方向发展
        if (info_gain > best_info_gain):
            best_info_gain = info_gain
            best_feature = i
    return best_feature


dataset = [[2,1,1,'yes'],[2,1,1,'yes'],[3,1,0,'no'],[4,1,1,'yes'],[0,1,1,'yes'], [0,1,0,'no'],[1,1,1,'yes']]
print dataset
print cal_shannon_ent(dataset)

print "----"

print split_data_set(dataset, 1, 1)

print "*" * 10
print choose_best_feature_split(dataset)
