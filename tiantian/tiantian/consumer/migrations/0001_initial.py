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
                ('address', models.CharField(default=b'\xe5\x8c\x97\xe4\xba\xac\xe6\xb5\xb7\xe6\xb7\x80\xe5\x8c\xba\xe4\xb8\xad\xe5\x85\xb3\xe6\x9d\x91\xe8\xbd\xaf\xe4\xbb\xb6\xe5\x9b\xad', max_length=100)),
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
