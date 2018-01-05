# coding=utf-8
import sys
sys.path.append("..")
from django.db import models
from goods.models import *
from cart.models import *
from consumer.models import *


# 订单模型  ---
class OrderInfo(models.Model):
	user = models.CharField(max_length=20)
	ototal = models.DecimalField(max_digits=10,decimal_places=2)
	state = models.BooleanField(default=False)
	# 订单编号
	onum = models.CharField(max_length=20)
	# 订单提交时间
	odata = models.DateTimeField()
	address = models.ForeignKey('consumer.UserInfo')


# 订单详情
class OrderDetailInfo(models.Model):
	order = models.ForeignKey('OrderInfo')
	goods = models.ForeignKey('goods.GoodsInfo')
	# CommaSeparatedIntegerField逗号分隔的整数，IntegerField 整数
	count = models.IntegerField(max_length=None)
	price = models.DecimalField(max_digits=20,decimal_places=2)
	# tprice = models.ForeignKey('cart.CartInfo')
	tprice = models.DecimalField(max_digits=20, decimal_places=2)
