# 打开views.py控制器写入操作
from django.shortcuts import render
from django.http import HttpResponse
from pandas import read_csv
import os
import sys

from mysite.utils.dataget import getdata#引入爬虫功能
from mysite.utils.gen_wc import gen_wc#引入词云功能
from mysite.utils.chart1 import bar#引入柱状图
# Create your views here.


 #定义一个主页的方法，参数为请求对象
 #函数返回经过render渲染的页面index.html
 #index.html在bapp下新建的templates目录中创建
def index(request):
    return render(request, 'mysite/index.html')


#点击跳转详细界面
def detail(request):
    if request.method == 'POST':
        #运行python爬虫，生成csv，跳转到二级页面
        a = getdata()
        return render(request,'mysite/detail.html')#又是一天，大概是要写明白from里的action路径，<form action="url">，然后要在url.py文件的path里写上（还是没太懂能跑就行


#二级页面按键1，显示详细列表(这里要基于txt生成一个csv还没弄（弄好了这里说一声
def get_data(request):
    if request.method == 'POST':
        #运行python爬虫
        #a = getdata()
        #在建立一个utils把要用到的py文件放进来再在views里面引用，最后像这个一样就可以完美运行了啊啊啊啊啊啊
        #那就不用那个收集数据的按钮了（把它去掉吗

        data_set = read_csv("C:/Users/Lenovo/Desktop/kmw/listcsv.csv")#可以用这个来生成详细列表界面，先留着
        data = data_set.values[:, :]
        list_data =[]
        for line in data:
            ls=[]
            for j in line:
                ls.append(j)
            list_data.append(ls)
        return render(request,'mysite/get_data.html',{'list_data':list_data})

#柱状图
def histogram(request):
    if request.method == 'POST':
        a = bar()
        return render(request,'mysite/bar.html')

#词云
def wordcloud(request):
    if request.method == 'POST':
        #运行词云生成程序
        a = gen_wc()
        return render(request,'mysite/basic_wordcloud.html')
