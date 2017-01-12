#coding:utf-8
from django.shortcuts import render,redirect
from models import *
from django.core.paginator import *
from cart.models import *
from consumer.models import *
from django.http import *
from tiantian.MyDecorator import *

#首页
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

	context = {'list': goodsList,"cartNum":cartNum}
	print(context)
	return render(request,"goods/index_shopping.html",context)

# 详情
def detail(request,id):
	id = int(id)
	if request.session.get('latest_goods_list'):
		latest_goods_list = request.session.get('latest_goods_list')
		latest_goods_list.insert(0,id)
		request.session['latest_goods_list'] = latest_goods_list
	else:
		latest_goods_list = []
		latest_goods_list.insert(0,id)
		request.session['latest_goods_list'] = latest_goods_list
	list = GoodsInfo.objects.get(id=id)
	# 通过过滤取出对应的商品分类且是新品的商品
	list1 = GoodsInfo.objects.filter(gnews='news',gtype=list.gtype)[:2]
	cartNum = 0
	if request.session.has_key('id'):
		user_id = request.session.get('id')
		cart = CartInfo.objects.filter(user_id=user_id)
		cartNum = cart.count
	context = {'goods':list,'list1':list1,"cartNum":cartNum}
	return render(request,"goods/base_detail.html",context)


# 列表页
def list(request,id,pIndex):
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

	context = {'list':list,'list1':list1,"list2": list2,'pIndex': pIndex, "plist": plist,'id':id,'length':length}
	return render(request,"goods/goods_list.html",context)


#立即购买
def immediatelyBuy(request,id):
	#user_id = request.session.get('id')  # 获取用户名???存ID比较好
	uid = 1
	# cartlist = CartInfo.objects.filter(user_id=uid,goods_id=id)
	goodsList = GoodsInfo.objects.filter(id=id)
	# context = {'cartlist': cartlist,"goods":goods}
	context = {"goodsList": goodsList}
	return render(request, 'order/place_order.html', context)


# 添加购物车
def addCart(request):
	num = request.POST.get('num', default=1)
	good_id = request.POST['value']
	user_id = request.session.has_key('id')
	if user_id:
		cart = CartInfo.objects.filter(user_id=user_id,good_id=good_id)
		cart.count = num
		cart.save()
	else:
		return redirect(request,"/consumer/login")
	return HttpResponse("ok")

#首页上面的登录,注册,注销,用户中心,我的购物车,我的订单按钮
def login(request):
	return redirect('/consumer/login/')


def register(request):
	return redirect('/consumer/register/')


def logout(request):
	del request.session['id'] 
	del request.session['uname']
	return redirect('/goods/')

@IsLogin
def userCenter(request):
	return redirect('/consumer/user_center_info/')

@RequireLogin
@IsLogin
def cart(request,context):
	return render(request, 'cart/cart.html', context)

@RequireLogin
@IsLogin
def order(request,context):
	return render(request, 'order/user_center_order.html', context)
