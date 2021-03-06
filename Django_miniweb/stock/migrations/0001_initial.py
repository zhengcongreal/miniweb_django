# Generated by Django 2.2.5 on 2020-10-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Focus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('note_info', models.CharField(default='', max_length=200, verbose_name='备注信息')),
            ],
            options={
                'db_table': 'tb_focus',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, verbose_name='股票代码')),
                ('short', models.CharField(max_length=10, verbose_name='股票简称')),
                ('chg', models.CharField(max_length=10, verbose_name='涨跌幅')),
                ('turnover', models.CharField(max_length=255, verbose_name='换手率')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='最新价')),
                ('highs', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='前期高点')),
                ('time', models.DateField(verbose_name='前期高点日期')),
            ],
            options={
                'db_table': 'tb_info',
            },
        ),
    ]
