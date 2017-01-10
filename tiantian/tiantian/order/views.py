#coding=utf-8
from django.shortcuts import render
import MySQLdb
from models import OrderInfo,OrderDetailInfo

#提交订单页面
def placeOrder(request):
	#session 获取id
	user_id = request.session.get('id')
	#订单总览：从购物车获取已选择的商品
	orderinfo = CartInfo.objects.filter(user_id=user_id)
	#获取订单详情
	orderdetailsinfo = OrderDetailInfo.objects.filter(order_id=orderinfo.id)
	#判断支付状态
	if OrderInfo.state==True:
		context = {'orderinfo':orderinfo,'orderdetailsinfo':orderdetailsinfo}
		return render(request,'order/user_center_order.html',context)

#订单总览页面
def userCenterOrder(request):
	#session 获取id
	user_id = request.session.get('id')
	#订单总览：从购物车获取已选择的商品
	orderinfo = CartInfo.objects.filter(user_id=user_id)
	#判断，点击去付款，返回提交订单页面
	if OrderInfo.state==False:
		context = {'orderinfo':orderinfo}
		#返回的提交订单页面
		return render(request,'order/place_order.html',context) 

#订单详情页面
def orderDetailsInfo(request):
	#session 获取id
	user_id = request.session.get('id')
	#获取订单详情
	orderdetailsinfo = OrderDetailInfo.objects.filter(order_id=orderinfo.id)
	context = {'orderdetailsinfo':orderdetailsinfo}
	return render(request,'order/order_details_info.html',context)

