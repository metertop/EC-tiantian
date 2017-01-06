#coding=utf-8
from django.db import models

class UserInfo(models.Model):
	# 用户信息
	uname = models.CharField(max_length=20)
	upwd = models.CharField(max_length=150)	
	utel = models.CharField(max_length=40,default="18710063456")
	uemail = models.CharField(max_length=40)
	#address = models.CharField(max_length=100,default="北京海淀区中关村软件园")
	address = models.CharField(max_length=100,default="ChinaBeiJing")
	isDelete = models.BooleanField(default = False)
	class Meta():
		db_table = "userinfo"


class RecInfo(models.Model):
	#收件人地址信息
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	tel = models.CharField(max_length=40)
	postcode = models.CharField(max_length=20)
	isDelete = models.BooleanField(default=False)
	userNum = models.ForeignKey('UserInfo')
	class Meta():
		db_table = "recinfo"
