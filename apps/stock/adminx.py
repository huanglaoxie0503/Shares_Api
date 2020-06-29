#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 15:46
# @Author  : Oscar
import xadmin
from .models import StockInfo


class StockInfoAdmin(object):
    # 自定义显示字段
    list_display = ['stock_code', 'stock_name', 'stock_full_name', 'listing_date', 'registered_address']
    # 自定义搜索字段
    search_fields = ['stock_code', 'stock_name', 'stock_full_name', 'listing_date', 'registered_address']
    # 自定义过滤器字段
    list_filter = ['stock_code', 'stock_name', 'stock_full_name', 'listing_date', 'registered_address']
    # 自定义排序字段
    ordering = ['-stock_code']
    # 自定义只读字段
    readonly_fields = ['stock_code']
    # 自定义隐藏字段   readonly_fields 和 exclude 是冲突的，定义的字段不能一样。
    exclude = ['stock_name']


xadmin.site.register(StockInfo, StockInfoAdmin)