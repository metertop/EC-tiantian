# coding=utf-8
from django.contrib import admin
from models import *


class UserInfoAdmin(admin.ModelAdmin):
	list_display = ['uname', 'upwd','utel'
					,'uemail','address', 'isDelete']


class RecInfoAdmin(admin.ModelAdmin):
	list_display = ['name', 'address',
					'tel', 'postcode', 'isDelete', 'userNum']


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(RecInfo, RecInfoAdmin)
