 -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('consumer', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
                ('goods', models.ForeignKey(to='goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=20)),
                ('ototal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('state', models.BooleanField(default=False)),
                ('onum', models.CharField(max_length=20)),
                ('odata', models.DateTimeField()),
                ('address', models.ForeignKey(to='consumer.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='order.OrderInfo'),
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='tprice',
            field=models.ForeignKey(to='cart.CartInfo'),
        ),
    ]
