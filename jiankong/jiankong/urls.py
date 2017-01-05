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
from django.contrib.auth.views import login,logout_then_login
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', inapp.index, name="index"),
    url(r'^apiserverinfo', inapp.apiserverinfo),
    url(r'^addserver', inapp.addserver, name="addserver"),
    url(r'^serverinfo', inapp.serverinfo, name='serverinfo'),
    url(r'^serverlist', inapp.serverlist, name="serverlist"),
    url(r'^deleteserver',inapp.deleteServer,name="deleteserver"),
    url(r'^accounts/login/$',login, {'template_name': 'login/login.html'},name="login"),
    url(r'^accounts/logout/$',logout_then_login,name="logout"), #退出登陆
    url(r'^accounts/profile',RedirectView.as_view(url='/index')),
]