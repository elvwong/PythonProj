# -*- coding: utf-8 -*-
'''
Created on 2016年11月21日

@author: wangyong

使用MySQLdb必须保证Python是32位。
'''

import MySQLdb,sched
from glob import glob
from shutil import make_archive

class MyClass:

    def __init__(self, params): 
        
        print('Hello:'+params)
     
    def __new__(self):
        
        print('new----')
         
    def sayGY(self):
        
        print('Bye Bye!')

class MyChildClass(MyClass):
    
    def __init__(self):
        print('init')
        
    def connMySql(self):
        # 打开数据库连接
        conn = MySQLdb.connect("127.0.0.1","root","sa","pythondb" )

        # 使用cursor()方法获取操作游标 
        cursor = conn.cursor()
        '''
        conn= MySQLdb.connect(
                host='127.0.0.1',
                port = 3306,
                user='root',
                passwd='sa',
                db ='pythondb',
                )
        cursor = conn.cursor()
        '''
        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取一条数据库。
        data = cursor.fetchone()

        print "Database version : %s " % data
        
        # 关闭数据库连接
        conn.close()
        
    def createTab(self):
        # 打开数据库连接
        conn = MySQLdb.connect("127.0.0.1","root","sa","pythondb" )

        # 使用cursor()方法获取操作游标 
        cursor = conn.cursor()
        # 如果数据表已经存在使用 execute() 方法删除表。
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        
        # 创建数据表SQL语句
        sql = """CREATE TABLE EMPLOYEE (
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,  
                 SEX CHAR(1),
                 INCOME FLOAT )"""
        
        cursor.execute(sql)
        
        # SQL 插入语句
        sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
               LAST_NAME, AGE, SEX, INCOME) \
               VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
               ('tom', 'mr', 20, 'M', 2000)
        try:
            # 执行sql语句
            cursor.execute(sql)
            #data = cursor.rowcount()
            #print "result : %s " % data     
            # 提交到数据库执行
            conn.commit()
                   
        except:
            print "except---"   
            # 发生错误时回滚
            conn.rollback()
        # 关闭数据库连接
        conn.close()
           
mc=MyClass('王勇');    
mcc=MyChildClass();
mcc.connMySql();
#mcc.createTab();
#mcc.sayGY();    
mc.sayGY();
