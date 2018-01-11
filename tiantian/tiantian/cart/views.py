# coding=utf-8
from django.shortcuts import render
from order.models import OrderInfo,OrderDetailInfo
from django.http import JsonResponse
from models import CartInfo
from consumer.models import UserInfo, RecInfo
import json
from django.views.decorators.csrf import csrf_exempt
import time
from tiantian.OrderUtil import order_num


# 购物车主页，根据session找到用户id，从CartInfo中查数据
def cart(request):
    uid = request.session.get('id')
    cartlist = CartInfo.objects.filter(user_id=uid)
    context = {'cartlist': cartlist}
    return render(request, 'cart/cart.html', context)


# 购物车页面点击删除时，调用此函数，根据传过来的id，删除CartInfo中的对象
@csrf_exempt
def remove_cart(request):
    cartid = request.POST['cartid']
    cartinfo = CartInfo.objects.get(pk=cartid)
    cartinfo.delete()
    return JsonResponse({'ok':'ok'})


# 接受返回的数据，格式为querydic,{u"count":[, ], u"ototal":[, ], u"price":[, ], u"goods":[, ], }
@csrf_exempt
def to_order(request):
    dict1 = request.POST
    user = request.session.get('id')
    ototal = dict1.get('ototal')
    o_date = time.strftime("%Y-%m-%d %H:%M:%S")
    o_num = order_num()
    user_add = RecInfo.objects.filter(userNum=user)
    # print(user)
    # print("u" * 20)
    # for u_a in user_add:
    #
    #     print(u_a.address)
    o_address = user_add[0].id  # 暂时默认
    print('ccc'*20)
    print(ototal)
    orderinfo = OrderInfo.objects.create(user=user, ototal=ototal, state=False, odata=o_date, address_id=o_address, onum=o_num)
    order = orderinfo
    goodslist = dict1.getlist('goods')
    countlist = dict1.getlist('count')
    pricelist = dict1.getlist('price')
    cartidlist = dict1.getlist('cart_id')
    for i in range(len(goodslist)):
        cartid = cartidlist[i]
        cartinfo = CartInfo.objects.get(pk=cartid)
        # goods = goodslist[i]
        goods = cartinfo.goods
        count = countlist[i]
        price = pricelist[i]
        orderdetail = OrderDetailInfo.objects.create(order=order, goods=goods, count=count, price=price, tprice=ototal)
        cartinfo.delete()

    return JsonResponse({"ok": "ok"})

