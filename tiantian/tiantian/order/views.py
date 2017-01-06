#coding=utf-8
from django.shortcuts import render
import MySQLdb
from models import OrderInfo,OrderDetailInfo

def placeOrder(request):
	#session 获取id
	user_id = request.session.get('id')
	#从购物车获取已选择的商品 订单
	orderinfo = OrderInfo.objects.filter(user=user_id)
	#获取订单详情
	orderdetailsinfo = OrderDetailInfo.objects.filter(order=orderinfo)
	context = {'orderinfo':orderinfo,'orderdetailsinfo':orderdetailsinfo}
	return render(request,'order/place_order.html',context)


def userCenterOrder(request):
	return render(request,'order/user_center_order.html') 

def orderDetailsInfo(request):
	return render(request,'order/order_details_info.html')

