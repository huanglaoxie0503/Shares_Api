from django.shortcuts import render
from django.http import HttpResponse

from apps.utils import email
# Create your views here.


def index(request):
    email.send_register_email.dealy()
    return HttpResponse('邮件发送成功，请注意查收。')


