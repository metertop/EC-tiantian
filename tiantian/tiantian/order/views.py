#coding=utf-8
from django.shortcuts import render
from django.core.paginator import Paginator
import MySQLdb
from models import OrderInfo, OrderDetailInfo
from django.views.decorators.csrf import csrf_exempt
from tiantian.MyDecorator import *


# 提交订单页面
@IsLogin
def placeOrder(request, context):
    # session 获取id
    user_id = request.session.get('id')
    # 订单总览：从购物车获取已选择的商品，购物车已传入数据到OrderInfo，OrderDetailInfo
    orderinfo = OrderInfo.objects.filter(user=user_id)
    # 获取订单详情
    orderdetailsinfo = OrderDetailInfo.objects.filter(order=orderinfo[0].id)
    context_order = {'orderinfo': orderinfo, 'orderdetailsinfo': orderdetailsinfo, 'uname': context['uname']}
    return render(request, 'order/user_center_order.html', context_order)


# 订单总览页面
@IsLogin
def userCenterOrder(request, context):
    #session 获取id
    user_id = request.session.get('id')
    # 订单总览：从购物车获取已选择的商品，购物车已传入数据到OrderInfo，OrderDetailInfo
    orderinfo = OrderInfo.objects.filter(user=user_id)
    order_context = {"uname": context['uname']}
    order_count = len(orderinfo)
    if order_count != 0:
        #获取订单详情
        order_details_info = OrderDetailInfo.objects.filter(order=orderinfo).order_by('-id')
        order_context.update({'orderinfo': orderinfo, 'orderdetailsinfo': order_details_info, 'order_count': order_count})
    return render(request,'order/user_center_order.html', order_context)


# 分页
def pageTab(request,Pindex):
    list1 = OrderInfo.objects.filter(user=user_id)
    p = Paginator(list1, 10)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    context = {'list': list2, 'plist': plist, 'pIndex': pIndex}
    return render(request, 'order/user_center_order.html', context)




        




