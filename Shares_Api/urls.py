"""Shares_Api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.generic import TemplateView

from users.views import LoginView, Register, ActiveUserView, ForgetPwdView, ReSetView

import xadmin

urlpatterns = [
    # path(r'admin/', admin.site.urls),
    path(r'xadmin/', xadmin.site.urls),

    path(r'captcha/', include('captcha.urls')),

    path(r'', TemplateView.as_view(template_name='index.html'), name='index'),
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'register/', Register.as_view(), name='register'),
    path(r'forget/', ForgetPwdView.as_view(), name='forget'),

    # 激活邮箱
    re_path(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    # 重置密码
    re_path(r'^reset/(?P<active_code>.*)/$', ReSetView.as_view(), name='reset_pwd'),
    re_path(r'^reset/(?P<active_code>.*)/$', ReSetView.as_view(), name='reset'),
]
