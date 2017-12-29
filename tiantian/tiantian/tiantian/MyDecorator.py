# coding:utf-8
from django.shortcuts import redirect

# 判断用户是否登录
def IsLogin(func):
    def isLogin(request, *args, **kwargs):
        context = {}
        if request.session.has_key('uname'):
            context['uname'] = request.session['uname']
        return func(request, context, *args, **kwargs)
    return isLogin


def RequireLogin(func):
    def requireLogin(request,*args,**kwargs):
        if not request.session.has_key('id'):
            return redirect('/consumer/login/')
        else:
            return func(request,*args,**kwargs)
    return requireLogin
