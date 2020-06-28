from django.db import models

# Create your models here.


class FactorInfo(models.Model):
    """
    因子基本信息
    """
    factor_id = models.IntegerField(verbose_name='因子ID', default=0)
    factor_name = models.CharField(max_length=100, verbose_name='因子名称')
    factor_desc = models.CharField(max_length=500, verbose_name='因子描述', default='')

    class Meta:
        db_table = 'factor_info'
        verbose_name = '因子'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.factor_name
