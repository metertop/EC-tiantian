#coding=utf-8
from django.db import models

class UserInfo(models.Model):
	# 用户信息
	uname = models.CharField(max_length=20)
	upwd = models.CharField(max_length=20)	
	uemail = models.CharField(max_length=40)
	isDelete = models.BooleanField(default = False)
	class Meta():
		db_table = "userinfo"


class RecInfo(models.Model):
	#收件人地址信息
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	tel = models.CharField(max_length=20)
	postcode = models.CharField(max_length=20)
	isDelete = models.BooleanField(default=False)
	userNum = models.ForeignKey('UserInfo')
	class Meta():
		db_table = "recinfo"
