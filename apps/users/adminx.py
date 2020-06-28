#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 15:20
# @Author  : Oscar
import xadmin
from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    # 自定义显示字段
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 自定义搜索字段
    search_fields = ['code', 'email', 'send_type']
    # 自定义过滤器字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


# 注册
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)