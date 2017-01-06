<<<<<<< HEAD
#coding=utf-8
=======
<<<<<<< HEAD
#coding:utf-8
=======
#coding=utf-8
>>>>>>> a4026c127372c4982f47e3d1fad8f6937db99453
>>>>>>> d3234dc8c9150c4c0208250253af567e0c9d32b0
from django.db import models

class UserInfo(models.Model):
	# 用户信息
	uname = models.CharField(max_length=20)
<<<<<<< HEAD
	upwd = models.CharField(max_length=150)	
	utel = models.CharField(max_length=40,default="18710063456")
=======
	upwd = models.CharField(max_length=20)
>>>>>>> 3149d691db60493580e578a0b9852f89af6a772d
	uemail = models.CharField(max_length=40)
	#address = models.CharField(max_length=100,default="北京海淀区中关村软件园")
	address = models.CharField(max_length=100,default="ChinaBeiJing")
	isDelete = models.BooleanField(default = False)
	class Meta():
		db_table = "userinfo"


class RecInfo(models.Model):
<<<<<<< HEAD
	#收件人地址信息
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	tel = models.CharField(max_length=40)
	postcode = models.CharField(max_length=20)
	isDelete = models.BooleanField(default=False)
	userNum = models.ForeignKey('UserInfo')
	class Meta():
		db_table = "recinfo"
<<<<<<< HEAD
=======
=======
    #收件人地址信息
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    userNum = models.ForeignKey('UserInfo')
    class Meta():
        db_table = "recinfo"
>>>>>>> 3149d691db60493580e578a0b9852f89af6a772d
>>>>>>> d3234dc8c9150c4c0208250253af567e0c9d32b0
