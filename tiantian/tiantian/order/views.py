from django.shortcuts import render


def placeOrder(request):
	return render(request,'order/place_order.html') 
def userCenterOrder(request):
	return render(request,'order/user_center_order.html') 
def orderDetailsInfo(request):
	return render(request,'order/order_details_info.html')

