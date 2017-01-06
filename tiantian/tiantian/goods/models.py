#coding:utf-8
from django.db import models


#商品分类
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=0)

    def __str__(self):
        return self.ttitle.encode('utf-8')

    class Meta():
        db_table = "typeInfo"


#商品
class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=50)
    gprice = models.DecimalField(max_digits=10,decimal_places=2)
    gdesc = models.TextField(max_length=300)
    gimgAdd = models.ImageField(upload_to='img')
    isDelete = models.BooleanField(default=0)
    gtype = models.ForeignKey('TypeInfo')

    def __str__(self):
        return self.ttitle.encode('utf-8')

    class Meta():
        db_table="goodsInfo"
