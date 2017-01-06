from django.contrib import admin

from models import *

class GoodsInfoInline(admin.StackedInline):
    model = GoodsInfo

class TypeInfoInline(admin.ModelAdmin):
    inlines = [GoodsInfoInline]
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['ttitle']

admin.site.register(TypeInfo, TypeInfoInline)
