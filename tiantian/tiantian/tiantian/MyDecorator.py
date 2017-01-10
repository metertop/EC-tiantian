# coding:utf-8
from django.shortcuts import redirect

#判断用户是否登录
def IsLogin(func):
    def isLogin(request):
        context = {}
        if request.session.has_key('uname'):
            context['uname'] = request.session['uname']
        return func(request,context)
    return isLogin


def RequireLogin(func):
    def requireLogin(request):
        if not request.session.has_key('id'):
            return redirect('/consumer/login/')
        else:
            return func(request)
    return requireLogin
