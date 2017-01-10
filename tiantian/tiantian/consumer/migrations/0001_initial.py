# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=40)),
                ('postcode', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'recinfo',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=150)),
                ('utel', models.CharField(default=b'18710063456', max_length=40)),
                ('uemail', models.CharField(max_length=40)),
                ('address', models.CharField(default=b'ChinaBeiJing', max_length=100)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.AddField(
            model_name='recinfo',
            name='userNum',
            field=models.ForeignKey(to='consumer.UserInfo'),
        ),
    ]
