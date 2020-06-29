#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 17:28
# @Author  : Oscar
import os
import django

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Shares_Api.settings')

app = Celery('MxOnline')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)