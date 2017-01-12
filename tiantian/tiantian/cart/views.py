# coding=utf-8
from django.shortcuts import render
from order.models import OrderInfo,OrderDetailInfo
from django.http import JsonResponse
from models import CartInfo
import json


# 购物车主页，根据session找到用户id，从CartInfo中查数据
def cart(request):
    uid = request.session.get('id')
    cartlist = CartInfo.objects.filter(user_id=uid)
    context = {'cartlist':cartlist}
    return render(request, 'cart/cart.html', context)


# 购物车页面点击删除时，调用此函数，根据传过来的id，删除CartInfo中的对象
def remove_cart(request):
    cartid = request.POST['cartid']
    cartinfo = CartInfo.objects.get(pk=cartid)
    cartinfo.delete()
    return JsonResponse({'ok':'ok'})

# 接受返回的数据，格式为querydic,{u"count":[, ], u"ototal":[, ], u"price":[, ], u"goods":[, ], }
def to_order(request):
    dict = request.POST

    user = request.session.get('id')
    ototal = dict.get('ototal')
    orderinfo = OrderInfo.objects.create(user=user, ototal=ototal, state=False,)

    order = orderinfo.id
    goodslist = dict.getlist('goods')
    countlist = dict.getlist('count')
    pricelist = dict.getlist('price')
    cartidlist = dict.getlist('cart_id')
    for i in range(len(goodslist)):
        goods = goodslist[i]
        count = countlist[i]
        price = pricelist[i]
        cartid = cartidlist[i]
        orderdetail = OrderDetailInfo.objects.create(order=order, goods=goods, count=count, price=price)
        cartinfo = CartInfo.objects.get(pk=cartid)
        cartinfo.delete()

    return JsonResponse({"ok":"ok"})

