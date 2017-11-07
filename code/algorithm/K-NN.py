#！usr/bin/env python 3.6
#copy right 2017  NoWay2Home



import numpy as np
import operator

def create_data():
    group = np.array([[1,101],[5,89],[108,5],[115,8]])
    labels =['爱情片','爱情片','动作片','动作片']
    return group,labels

"""
func :kNN
"""
def classify(inx,data_set,labels,k):
    #返回data_set的行数
    data_set_size = data_set.shape[0]
    #求输入参数，在每行上域原始参数数据的差值
    diff_mat = np.tile(inx,(data_set_size,1))-data_set
    #求差值的平方
    sq_diff_mat = diff_mat**2
    #将所有数据中的元素相加
    sq_distances = sq_diff_mat.sum(axis=1)
    #开发算出求距离
    distances = sq_distances**0.5
    #距离排序，从小到大
    sorted_distance_indices = distances.argsort()
    class_count = {}
    for i in range(k):
        #取出前K个元素的类别
        vota_label = labels[sorted_distance_indices[i]]
        #计算类别次数
        class_count[vota_label] = class_count.get(vota_label,0) + 1
    sorted_class_count = sorted(class_count.items(),key=operator.itemgetter(1),reverse=True)
    return sorted_class_count[0][0]


if __name__ == '__main__':
    group,labels = create_data()
    test = [101,20]
    test_class = classify(test,group,labels,3)
    print(test_class)

