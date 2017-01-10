# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address',
            field=models.CharField(default=b'ChinaBeiJing', max_length=100),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='utel',
            field=models.CharField(default=b'18710063456', max_length=40),
        ),
        migrations.AlterField(
            model_name='recinfo',
            name='tel',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(max_length=150),
        ),
    ]
