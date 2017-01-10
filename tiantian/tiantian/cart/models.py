from django.db import models

class CartInfo(models.Model):
    user = models.ForeignKey('consumer.UserInfo')
    goods = models.ForeignKey('goods.GoodsInfo')
    count = models.IntegerField()