"""jiankong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from opsapp import views as inapp
from wx import views as wx      #微信报警部分
from django.contrib.auth.views import login,logout_then_login
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', inapp.index),    #默认首页
    url(r'^admin/', admin.site.urls),
    url(r'^index', inapp.index, name="index"),
    url(r'^apiserverinfo', inapp.apiserverinfo, name="serverinfo"),
    url(r'^addserver', inapp.addserver, name="addserver"),
    url(r'^serverinfo/(\d+)/$', inapp.serverinfo, name='serverinfo'),
    url(r'^serverlist', inapp.serverlist, name="serverlist"),
    url(r'^deleteserver',inapp.deleteServer,name="deleteserver"),   #删除列表里卖弄的服务器
    url(r'^accounts/login/$',login, {'template_name': 'login/login.html'},name="login"),
    url(r'^accounts/logout/$',logout_then_login,name="logout"), #退出登陆
    url(r'^accounts/profile',RedirectView.as_view(url='/index')),
]
