"""
DjangoWebProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from mysite import views  # 从创建的功能应用中导入views模块
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),  #之前一直用的别人的path引用方法难怪404#要命啊卡死我了
    path('detail',views.detail,name='detail'),
    path('get_data',views.get_data,name='get_data'),
    path('histogram',views.histogram,name='histogram'),
    path('wordcloud',views.wordcloud,name='wordcloud')
]
