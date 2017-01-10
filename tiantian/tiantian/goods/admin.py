#coding:utf-8
from django.contrib import admin

from consumer.models import *
from models import *
from cart.models import *
from order.models import *


# class GoodsInfoInline(admin.StackedInline):
#     model = GoodsInfo
#     extra = 1
#
# class TypeInfoInline(admin.ModelAdmin):
#     inlines = [GoodsInfoInline]
    # search_fields：搜索字段，搜索框会出现在上侧

<<<<<<< HEAD

class TypeInfoInline(admin.ModelAdmin):
    list_display = ['id', 'ttitle','isDelete','title1','title2','title3','tImgAdd']


class GoodsInfoInline(admin.ModelAdmin):
    list_display = ['pk', 'gtitle', 'gprice', 'gdesc','gimgAdd','gimgDetail','gdetail','isDelete','gtype']

admin.site.register(TypeInfo,TypeInfoInline)
admin.site.register(GoodsInfo,GoodsInfoInline)


=======
# class TypeInfoInline(admin.ModelAdmin):
#     list_display = ['id', 'ttitle','isDelete','title1','title2','title3','tImgAdd']
#
#
# class GoodsInfoInline(admin.ModelAdmin):
#     list_display = ['pk', 'gtitle', 'gprice', 'gdesc','gimgAdd','gimgDetail','gdetail','isDelete','gtype']
#
# admin.site.register(TypeInfo,TypeInfoInline)
# admin.site.register(GoodsInfo,GoodsInfoInline)
>>>>>>> 94d66d135b536d19b3b87568b911fa7e50e6312c
