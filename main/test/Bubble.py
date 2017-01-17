# -*- coding: UTF-8 -*-
'''
Created on 2017年1月11日

@author: wangyong
'''


def bubble(l):  
    seq = range(3)
    enu = enumerate('qwe')
    print l  
    for index in range(len(l) - 1, 0 , -1):  
        for two_index in range(index):  
            if l[two_index] > l[two_index + 1]:  
                l[two_index], l[two_index + 1] = l[two_index + 1], l[two_index]  
    print l  

def mybubble(l):
    for index ,item in enumerate(l):
        pass   
#l = [10, 20, 40, 50, 30, 60]    

def bubble1():    
    array = [1, 2, 5, 3, 6, 8, 4]
    for i in range(len(array) - 1, 0, -1):
        print 'i=:',i
        
        for j in range(0, i):
            print j
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        print array       
    print array
    
if __name__ == '__main__':
    #l = raw_input('请输入数字，用空格分割：').split()
    
    #for index, item in enumerate(l):
        #l[index] = int(item)
    #bubble(l)
    bubble1()
    