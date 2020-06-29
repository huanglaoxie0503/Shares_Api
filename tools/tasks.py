#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 11:34
# @Author  : Oscar
from celery import Celery

app = Celery('hello', broker='redis://localhost:6379/0')


@app.task
def hello():
    return 'hello world'


