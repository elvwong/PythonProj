#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wmi
import os 
import sys 
import platform 
import time 
from functools import wraps

#命名关键字 参数 python3 才支持！
#def person(name,age,*,city,job):
#    pass
    
def decodemo1(func):
    def _deco():
        print 'before demo :1'
        func()
        print 'after demo :1'
    return _deco    

def decodemo2(func):
    def _deco():
        print 'before demo :2'
        func()
        print 'after demo :2'
    return _deco

def decodemo3(arg):    
    def _deco(func):
        @wraps(func) # 没有的话会报错 ：'NoneType' object is not callable！因为修改了参数！
        def __deco():
            print 'before demo :3'
            func(arg)
            print 'after demo :3'
        return __deco
    return _deco

@decodemo1
@decodemo2
@decodemo3('go')
def demo(arg='hello'):
    print 'demo',arg

demo() 

if __name__=="__main__":
   pass

