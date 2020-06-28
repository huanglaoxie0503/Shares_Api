from django.db import models

from apps.users.models import UserProfile
from apps.stock.models import StockInfo

# Create your models here.


class UserAsk(models.Model):
    """
    用户咨询
    """
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机号码')
    product_name = models.CharField(max_length=100, verbose_name='产品名称')
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户产品咨询'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0, verbose_name='数据类型id')
    fav_type = models.IntegerField(choices=((1, '股票'), (2, '因子'), (3, '新闻')), default=1, verbose_name='收藏类型')
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    """
    用户消息
    """
    user = models.IntegerField(default=0, verbose_name='接收用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name


class StockComments(models.Model):
    """
    股票评论
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    stock = models.ForeignKey(StockInfo, verbose_name='股票', on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '股票评论'
        verbose_name_plural = verbose_name


class OptionalShares(models.Model):
    """
    自选股
    """
    user = models.ForeignKey(UserProfile, verbose_name='用户', on_delete=models.CASCADE)
    stock = models.ForeignKey(StockInfo, verbose_name='股票', on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name='添加时间', auto_now_add=True)

    class Meta:
        verbose_name = '自选股'
        verbose_name_plural = verbose_name
