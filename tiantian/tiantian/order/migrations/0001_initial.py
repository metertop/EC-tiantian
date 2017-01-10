# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=20)),
                ('goods', models.CharField(max_length=20)),
                ('count', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'cartinfo',
            },
        ),
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods', models.CharField(max_length=20)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=20)),
                ('ototal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='order.OrderInfo'),
        ),
    ]
