# coding=utf-8
from django.shortcuts import render
from order.models import OrderInfo,OrderDetailInfo

from models import CartInfo


def cart(request):
    # uid = request.COOKIES['id']  # 获取用户名???存ID比较好
    uid = 1
    cartlist = CartInfo.objects.filter(user_id=uid)
    context = {'cartlist':cartlist}
    return render(request, 'cart/cart.html', context)


def remove_cart(request):
    # 购物车页面点击删除时，调用此函数，根据传过来的id，删除CartInfo中的对象
    cartid = request.POST['cartid']
    cartinfo = CartInfo.objects.get(pk=cartid)
    cartinfo.delete()
    # return JsonResponse({'ok':'ok'})


def to_order(request):
    dict = request.POST
    print dict
    user = request.SESSIONS.get['id']
    ototal = dict['ototal']
    print user
    print ototal
    orderinfo = OrderInfo.objects.create(user=user, ototal=ototal, )

    order = orderinfo.id
    for temp in dict['goodsinfo']:
        state = temp['state']
        goods = temp['goods']
        count = temp['count']
        price = temp['price']
        print state,goods,count,price
        orderdetail = OrderDetailInfo.objects.create(order=order, state=state, goods=goods, count=count, price=price)

