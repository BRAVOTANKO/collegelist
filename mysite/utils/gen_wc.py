from pyecharts.charts import WordCloud
import pandas as pd
import pyecharts.options as opts

WordCloud=WordCloud()

def main(name):
    wd = pd.read_csv('listcsv.csv')
    word = [i[0] for i in wd[['大学']].values]
    value = [i[0] for i in wd[['总分']].values]
    
    #print(word)
    #print(value)
    data = list(zip(word,value))
    #print(data)
    

    name.add(series_name="大学排名", data_pair=data, word_size_range=[6, 66])
    name.set_global_opts(
            title_opts=opts.TitleOpts(
                title="大学排名", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    name.render("C:/Users/Lenovo/Desktop/kmw/DjangoWebProject1/mysite/templates/mysite/basic_wordcloud.html")#生成一个显示词云图的html页面


def gen_wc():
    main(WordCloud)


