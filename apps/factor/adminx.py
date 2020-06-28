#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 15:51
# @Author  : Oscar
import xadmin
from .models import FactorInfo


class FactorInfoAdmin(object):
    # 自定义显示字段
    list_display = ['factor_id', 'factor_name', 'factor_desc']
    # 自定义搜索字段
    search_fields = ['factor_id', 'factor_name', 'factor_desc']
    # 自定义过滤器字段
    list_filter = ['factor_id', 'factor_name', 'factor_desc']


# 注册
xadmin.site.register(FactorInfo, FactorInfoAdmin)