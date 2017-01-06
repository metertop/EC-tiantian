#coding:utf-8
from django.db import models


#商品分类
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=30)
    title1 = models.CharField(max_length=30)
    title2 = models.CharField(max_length=30)
    title3 = models.CharField(max_length=30)
    tImgAdd = models.ImageField(upload_to='img')
    typeId = models.IntegerField()
    isDelete = models.BooleanField(default=0)

    def __unicode__(self):
        return self.ttitle

    class Meta():
        db_table = "typeInfo"


#商品
class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=50)
    gprice = models.DecimalField(max_digits=10,decimal_places=2)
    gdesc = models.TextField(max_length=300)
    gimgAdd = models.ImageField(upload_to='img')
    gimgDetail = models.ImageField(upload_to='img')
    isDelete = models.BooleanField(default=0)
    gdetail = models.TextField(max_length=300)
    gnews = models.CharField(max_length=20)
    gtype = models.ForeignKey('TypeInfo')

    def __unicode__(self):
        return self.gtitle

    class Meta():
        db_table="goodsInfo"
