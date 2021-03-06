#coding:utf-8
from django.shortcuts import render,redirect
from models import *
from django.core.paginator import *
from cart.models import *
from consumer.models import *
from order.models import *
from django.http import *
from tiantian.MyDecorator import *
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from tiantian.OrderUtil import order_num
import time

# 首页
@IsLogin
def index(request,context):
	goodsList = []
	typeInfo = TypeInfo.objects.all()

	cartNum = 0
	if request.session.has_key('id'):
		user_id = request.session.get('id')
		cart = CartInfo.objects.filter(user_id=user_id)
		cartNum= cart.count

	for type in typeInfo:
		list = GoodsInfo.objects.filter(gtype_id=type.id)[:4]
		# 列表不为空进行添加
		if list:
			goodsList.append(list)

	goodsContext = {"list":goodsList,"cartNum":cartNum}

	# print('--------' + context['uname'])
	#if context['uname']:
	if request.session.has_key('uname'):
		goodsContext = {"uname":context['uname'], "list": goodsList,"cartNum":cartNum}
	else:
		goodsContext = {'list': goodsList,"cartNum":cartNum}

	print(goodsContext)
	return render(request,"goods/index_shopping.html",goodsContext)


# 详情

@IsLogin
def detail(request, context, id):
	# id = int(id)
	if request.session.get('latest_goods_list'):
		latest_goods_list = request.session.get('latest_goods_list')
		latest_goods_list.insert(0,id)
		request.session['latest_goods_list'] = latest_goods_list
	else:
		latest_goods_list = []
		latest_goods_list.insert(0, id)
		request.session['latest_goods_list'] = latest_goods_list
	list = GoodsInfo.objects.get(id=id)
	# 通过过滤取出对应的商品分类且是新品的商品
	list1 = GoodsInfo.objects.filter(gnews='news',gtype=list.gtype)[:2]
	cartNum = 0
	if request.session.has_key('id'):
		user_id = request.session.get('id')
		cart = CartInfo.objects.filter(user_id=user_id)
		cartNum = cart.count
	context = {'goods': list, 'list1': list1, "cartNum": cartNum, "uname":context['uname']}
	return render(request, "goods/base_detail.html", context)


# 列表页
@IsLogin
def list(request, context, id, pIndex):
	list = GoodsInfo.objects.filter(gtype_id=id)
	list1 = GoodsInfo.objects.filter(gtype_id=id,gnews='news')
	print list
	# 通过Paginator类获取每页显示15条信息
	p = Paginator(list, 5)

	if pIndex == "":
		pIndex = '1'

	# 将页数转化为整数
	pIndex = int(pIndex)

	#获取当前页上所有对象的列表
	list2 = p.page(pIndex)

	# 获取页码列表
	plist = p.page_range

	# 总页数
	length = len(plist)

	context = {'list':list,'list1':list1,"list2": list2,'pIndex': pIndex, "plist": plist,'id':id,'length':length, "uname":context['uname']}
	return render(request,"goods/goods_list.html",context)


#立即购买   {{address}}&nbsp;&nbsp;（{{name}}&nbsp;收）&nbsp;&nbsp;{{tel}}
@IsLogin
def immediatelyBuy(request, context):
	user_id = request.session.get('id')  # 获取用户名???存ID比较好
	dict1 = request.GET
	goods_id = dict1.get('g_id')
	goods_count = dict1.get('g_count')
	goodsInfo = GoodsInfo.objects.get(id=goods_id)
	goods_price = goodsInfo.gprice
	ototal = float(goods_price) * int(goods_count)
	print(u"立即购买页面")
	print(ototal)
	o_date = time.strftime("%Y-%m-%d %H:%M:%S")
	o_num = order_num()
	user_add = RecInfo.objects.filter(userNum=user_id)
	o_address = user_add[0].id  # 暂时默认
	user_info = UserInfo.objects.filter(id=user_id)
	orderinfo = OrderInfo.objects.create(user=user_id, ototal=ototal, state=False, odata=o_date, address_id=o_address,
										onum=o_num)
	order = orderinfo
	tranPay = 10    # 运费10元
	needPay = tranPay+ototal
	orderdetail = OrderDetailInfo.objects.create(order=order, goods_id=goods_id, count=goods_count, price=goods_price, tprice=ototal)
	b_context = {"goodsInfo": goodsInfo, "uname": context['uname'], 'addressInfos': user_add, 'orderdetailsinfo': orderdetail, 'tranPay':tranPay,'needPay':needPay}
	return render(request, 'order/place_order.html', b_context)


# 立即购买--提交订单
def submit_buy(request, orderid):
	# OrderInfo.objects.filter(id=orderid).update(state=True)    #   多条更新，使用 filter().update()

	# 以下是单条更新
	orderInfo = OrderInfo.objects.get(id=orderid)
	orderInfo.state = True
	orderInfo.save()
	return redirect('/order/userCenterOrder/')


# 添加购物车
@csrf_exempt
@RequireLogin
def addCart(request):
	num = request.POST.get('num', default=1)
	good_id = request.POST['value']
	user_id = request.session.get('id')
	# cart = CartInfo.objects.filter(user_id=user_id,good_id=good_id)
	cart = CartInfo()
	cart.user_id = user_id
	cart.goods_id = good_id
	cart.count = num
	cart.save()
	return HttpResponse('ok')


# 首页上面的登录,注册,注销,用户中心,我的购物车,我的订单按钮
def login(request):
	return redirect('/consumer/login/')


def register(request):
	return redirect('/consumer/register/')


def logout(request):
	del request.session['id'] 
	del request.session['uname']
	return redirect('/goods/')



# @IsLogin
def userCenter(request):
	return redirect('/consumer/user_center_info/')


@csrf_exempt
@RequireLogin
@IsLogin
def cart(request,context):
	uid = request.session.get('id')
	cartlist = CartInfo.objects.filter(user_id=uid)
	print("----" * 10)
	print(cartlist)
	cart_context = {'cartlist': cartlist, 'uname': context['uname']}
	return render(request, 'cart/cart.html', cart_context)


@RequireLogin
@IsLogin
def order(request, context):
	# return render(request, 'order/user_center_order.html', context)
	return redirect('/order/userCenterOrder/')