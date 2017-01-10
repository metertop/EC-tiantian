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
            field=models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac\xe6\xb5\xb7\xe6\xb7\x80\xe5\x8c\xba\xe4\xb8\xad\xe5\x85\xb3\xe6\x9d\x91\xe8\xbd\xaf\xe4\xbb\xb6\xe5\x9b\xad', max_length=100),
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
