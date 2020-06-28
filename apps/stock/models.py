from django.db import models

# Create your models here.


class StockInfo(models.Model):
    """
    股票基本信息
    """
    stock_code = models.CharField(max_length=20, verbose_name='股票代码')
    stock_name = models.CharField(max_length=50, verbose_name='股票简称')
    stock_full_name = models.CharField(max_length=100, verbose_name='股票全称', default='')
    listing_date = models.DateField(verbose_name='上市日期', default='')
    registered_address = models.CharField(max_length=200, verbose_name='注册地址', default='')

    class Meta:
        db_table = 'stock_info'
        verbose_name = '股票基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.stock_name
