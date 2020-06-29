#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 15:20
# @Author  : Oscar
import xadmin
from xadmin import views
from .models import EmailVerifyRecord


class BaseSetting(object):
    # 主题设置
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    # 网站左上角和底部标题修改
    site_title = "股票管理系统"
    site_footer = "股票在线网"
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    # 自定义显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 自定义搜索字段
    search_fields = ['code', 'email', 'send_type']
    # 自定义过滤器字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


# 注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

# xadmin 全局设置注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
