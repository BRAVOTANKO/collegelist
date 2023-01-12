from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd

def main():
    collegedata = pd.read_csv('listcsv.csv')
    word = [i[0] for i in collegedata[['大学']].values]
    value = [i[0] for i in collegedata[['总分']].values]


    bar = (
        Bar()
        .add_xaxis(word)#x轴数据
        .add_yaxis("大学总分柱状图", value)#y轴数据
        .set_global_opts(

            title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"),#title
            yaxis_opts=opts.AxisOpts(name="总分"),#y轴标签
            xaxis_opts=opts.AxisOpts(name="大学名称",axislabel_opts={"rotate":45}),#x轴标签，x轴标签旋转45°
            datazoom_opts=opts.DataZoomOpts(type_="slider")#底部缩放栏
            )
        .set_series_opts(
           
            markline_opts=opts.MarkLineOpts(
               data=[
                    opts.MarkLineItem(type_="min", name="最小值"),
                    opts.MarkLineItem(type_="max", name="最大值"),
                    opts.MarkLineItem(type_="average", name="平均值"),#最小值最大值平均值
                ] 
             ),
         )
    )
    bar.render("C:/Users/Lenovo/Desktop/kmw/DjangoWebProject1/mysite/templates/mysite/bar.html")

def bar():
    main()


