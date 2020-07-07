#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 14:04
# @Author  : Oscar
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """
    登录字段验证
    """
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8)


class RegisterForm(forms.Form):
    """
    注册字段验证
    """
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ForgetForm(forms.Form):
    """
    注册字段验证
    """
    email = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ReSetPwdForm(forms.Form):
    """
    重置密码
    """
    password1 = forms.CharField(required=True, min_length=8)
    password2 = forms.CharField(required=True, min_length=8)
