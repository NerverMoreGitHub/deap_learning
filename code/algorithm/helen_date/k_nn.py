# -*- coding: UTF-8 -*-
#!usr/env/bin python 3.6



from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np

def file2matrix(file_name):
    file = open(file_name)
    array_lines = file.readlines()
    number_of_lines = len(array_lines)
    return_matrix = np.zeros((number_of_lines,3))
    class_label_vector = []
    index = 0
    for line in array_lines:
        line = line.strip()
        list_line = line.split('\t')
        return_matrix[index,:] = list_line[0:3]
        if list_line[-1] == 'didntLike':
            class_label_vector.append(1)
        if list_line[-1] == 'smallDoses':
            class_label_vector.append(2)
        if list_line[-1] == 'largeDoses':
            class_label_vector.append(3)
        index += 1
    return return_matrix,class_label_vector

def show_data(dating_data_mat,dating_labels):
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=14)
    fig,axs = plt.subplots(nrows=2,ncols=2,sharex=False,sharey=False)#,figsize=(13,8))
    number_of_labels = len(dating_labels)
    labels_colors=[]
    for i in dating_labels:
        if i == 1:
            labels_colors.append('black')
        if i == 2:
            labels_colors.append('orange')
        if i == 3:
            labels_colors.append('red')
    axs[0][0].scatter(x=dating_data_mat[:,0],y=dating_data_mat[:,1],color=labels_colors,s=15,alpha=.5)
    axs0_title_text = axs[0][0].set_title(u'每年获得的飞行常客里程数域玩视频游戏所消耗时间比',FontProperties=font)
    axs0_xlabel_text = axs[0][0].set_xlabel(u'',FontProperties=font)
    axs0_ylabel_text = axs[0][0].set_ylabel(u'',FontProperties=font)
    plt.setp(axs0_title_text,size=9,weight='bold',color='red')
    plt.setp(axs0_xlabel_text,size=7,weight='bold',color='black')
    plt.setp(axs0_ylabel_text,size=7,weight='bold',color='black')
    plt.show()
if __name__ == '__main__':
    file_name = 'datingTestSet.txt'
    dating_data_mat,dating_labels = file2matrix(file_name)
    show_data(dating_data_mat,dating_labels)