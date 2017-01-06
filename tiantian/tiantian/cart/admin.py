from django.contrib import admin
from models import *
from goods.models import *
from consumer.models import *

# Register your models here.

admin.site.register(CartInfo,)
admin.site.register(UserInfo,)
admin.site.register(GoodsInfo)
admin.site.register(TypeInfo)
