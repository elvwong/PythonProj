# -*- coding: UTF-8 -*-
'''
Created on 2017年1月19日

@author: wangyong
'''
from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/')
def index():
    #return render_template('index.html')
    return 'Hello World!-派森'

@app.route('/user/<users>')  
def hello_world(users):  
    return 'Hello %s' % users  

tmp_time = 0

if __name__ == '__main__':  
    app.run(debug = True)  