#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 15:53
# @Author  : Oscar
import xadmin
from .models import UserAsk, UserFavorite, UserMessage, StockComments, OptionalShares


class UserAskAdmin(object):
    # 自定义显示字段
    list_display = ['name', 'mobile', 'product_name', 'add_time']
    # 自定义搜索字段
    search_fields = ['name', 'mobile', 'product_name']
    # 自定义过滤器字段
    list_filter = ['name', 'mobile', 'product_name', 'add_time']
    # 自定义图标
    model_icon = 'fa fa-address-book-o'


class UserFavoriteAdmin(object):
    # 自定义显示字段
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    # 自定义搜索字段
    search_fields = ['user', 'fav_id', 'fav_type']
    # 自定义过滤器字段
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    # 自定义显示字段
    list_display = ['user', 'message', 'has_read', 'add_time']
    # 自定义搜索字段
    search_fields = ['user', 'message', 'has_read']
    # 自定义过滤器字段
    list_filter = ['user', 'message', 'has_read', 'add_time']


class StockCommentsAdmin(object):
    # 自定义显示字段
    list_display = ['user', 'stock', 'comments', 'add_time']
    # 自定义搜索字段
    search_fields = ['user', 'stock', 'comments']
    # 自定义过滤器字段
    list_filter = ['user', 'stock', 'comments', 'add_time']


class OptionalSharesAdmin(object):
    # 自定义显示字段
    list_display = ['user', 'stock', 'add_time']
    # 自定义搜索字段
    search_fields = ['user', 'stock']
    # 自定义过滤器字段
    list_filter = ['user', 'stock', 'add_time']


# 注册
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(StockComments, StockCommentsAdmin)
xadmin.site.register(OptionalShares, OptionalSharesAdmin)


