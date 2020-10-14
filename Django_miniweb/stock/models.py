from django.db import models

# Create your models here.
class Info(models.Model):
    code=models.CharField(max_length=6,verbose_name="股票代码")
    short=models.CharField(max_length=10,verbose_name="股票简称")
    chg=models.CharField(max_length=10,verbose_name="涨跌幅")
    turnover=models.CharField(max_length=255,verbose_name="换手率")
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="最新价")
    highs=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="前期高点")
    time=models.DateField(verbose_name="前期高点日期")
    class Meta:
        db_table='tb_info'


class Focus(models.Model):
    id =models.IntegerField(primary_key=True)
    note_info=models.CharField(max_length=200,verbose_name="备注信息",default='')
    class Meta:
        db_table='tb_focus'