#coding:utf-8
from django.shortcuts import render,redirect
from hashlib import sha1
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from models import UserInfo,RecInfo
from django.views.decorators.csrf import csrf_exempt

#首页
def index(request):
	return HttpResponse("HELLO WORLD!!!")

#登陆
def login(request):
	remberName = request.COOKIES.get('remberName')
	if remberName:
		print(remberName)
		return render(request,"consumer/login.html",{'remberName':remberName})
	else:
		print(remberName)
		return render(request,"consumer/login.html")

#注册
def register(request):
		return render(request,"consumer/register.html")

#注册检查用户名是否存在
@csrf_exempt
def checkReName(request):
	namehad = request.POST['uname']
	#到数据库中查是否有该用户，有则返回给前端触发事件值1
	nameList = UserInfo.objects.filter(uname=namehad)
	if len(nameList) == 1:
		checkResult = 1
	else:
		checkResult = 0
	return JsonResponse({'checkResult':checkResult})

#注册数据处理
def registerHandle(request):
	if request.method == 'POST':
		#接收注册信息
		uname = request.POST['uname']
		upwd = request.POST['upwd']
		cpwd = request.POST['cpwd']
		uemail = request.POST['uemail']
		#判断是否同意用户使用协议
		if request.POST.get('allow') == 'on':
		
			#如果填写信息有空的回到本页
			if uname=='' or upwd=='' or cpwd=='' or uemail=='':
				#return redirect("/consumer/register/")
				context = {"errinfo":"注册信息有误!"}
				return render(request,"consumer/register.html",context)
			else:
				if upwd != cpwd:
					#return redirect("/consumer/register/")
					context = {"errinfo":"注册信息有误!"}
					return render(request,"consumer/register.html",context)
				
				else:
					#保存注册信息
					#sha1加密
					s1 = sha1()
					s1.update(upwd)
					upwd = s1.hexdigest()
					u = UserInfo()
					u.uname=uname
					u.uemail=uemail
					u.upwd=upwd
					u.save()
					return redirect("/consumer/index/")

		else:
			return redirect("/consumer/register")


#登陆检查用户名是否存在
@csrf_exempt
def checkUname(request):

	uname = request.POST['uname']
	nameList = UserInfo.objects.filter(uname=uname)
	if len(nameList) == 1:
		checkRight = 1
	else:
		checkRight = 0
	print(checkRight)
	return JsonResponse({'checkRight':checkRight})


# 登陆请求数据的处理
#@csrf_exempt
def loginHandle(request):
	if request.method == "POST":
		uname = request.POST['username']
		upwd = request.POST['pwd']

		#sha1加密
		s1 = sha1()
		s1.update(upwd)
		pwd = s1.hexdigest()
		
		print(pwd)
		try:			
			#查询提取用户信息
			user_list = UserInfo.objects.filter(uname=uname)
			if len(user_list) == 0:  #没有该用户
				context = {"errinfo":"用户名或密码错误!"}
				return render(request,"consumer/login.html",context)
			elif user_list[0].upwd == pwd:
				save_id = user_list[0].id
				request.session['id'] = save_id
				flag = request.POST.get('isrember', default='')
				#勾选记住用户名
				if flag == "on":
					response = HttpResponseRedirect("/consumer/user_center_info/")
					#response = HttpResponse()
					#print("这是要写入的cookie:%s"%flag)
					print(uname)
					response.set_cookie('remberName', uname,3600)
					return response
				#return redirect("/consumer/index/")
				else:
					response = HttpResponseRedirect("/consumer/user_center_info/")
					#清理cookie里保存remberName
					response.delete_cookie('remberName')
					return response

				return redirect("/goods/")
			
			else:
				# 密码错误!
				context = {"errinfo":"用户名或密码错误!"}
				return render(request,"consumer/login.html",context)

		except Exception,e:
			print(e)

# 用户退出
def loginout(request):
	del request.session['id'] 
	return redirect('/consumer/index/')

#跳转到用户中心个人信息页面
def user_center_info(request):
	get_id = request.session.get('id')
	user_list = UserInfo.objects.filter(id=get_id)
	context = {
				'name':user_list[0].uname,
				'tel':user_list[0].utel,
				'address':user_list[0].address
				}
	return render(request,'consumer/user_center_info.html',context)

#跳转到用户中心收货地址页面
def user_center_site(request):
	get_id = request.session.get('id')
	addrList = RecInfo.objects.filter(userNum_id=get_id)
	print("*****************")
	for a in addrList:
		print(a.name)
		print(a.address)
		print(a.tel)
	user_list = UserInfo.objects.filter(id=get_id)
	#name = "("+user_list[0].uname+" receive)"
	name = user_list[0].uname
	context = {
				'name':name,
				'tel':user_list[0].utel,
				'address':user_list[0].address,
				'addrList':addrList
				}
	return render(request,'consumer/user_center_site.html',context)

#保存收件人信息
def recInfoHandle(request):
	get_id = request.session.get('id')
	if request.method == 'POST':
		name = request.POST['name']
		tel = request.POST['tel']
		address = request.POST['address']
		postcode = request.POST['postcode']
		userNum = get_id
		
		if name=='' or tel=='' or address=='' or postcode=='':
			return redirect("/consumer/user_center_site/")
		else:
			recinfo = RecInfo()
			recinfo.name = name 
			recinfo.address = address
			recinfo.tel = tel
			recinfo.postcode = postcode
			recinfo.userNum_id = userNum
			recinfo.save()
			return redirect("/consumer/user_center_site/")
