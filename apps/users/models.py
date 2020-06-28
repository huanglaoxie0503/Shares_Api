from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    自定义 UserProfile 继承自 AbstractUser，覆盖 django 自带的 user 信息
    """
    nick_name = models.CharField(max_length=20, verbose_name="花名", default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='male')
    address = models.CharField(max_length=200, verbose_name='家庭住址', default='')
    mobile = models.CharField(max_length=11, verbose_name='电话号码', null=True, blank=True)
    head_portrait = models.ImageField(max_length=100, verbose_name='头像', upload_to='image/%Y/%m',
                                      default='image/default.png')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    """
    验证码
    """
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', '注册'), ('forget', '找回密码')))
    send_time = models.DateTimeField(verbose_name='发送时间', auto_now_add=True)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
