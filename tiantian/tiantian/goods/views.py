from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"goods/index_shopping.html")


def list(request):
    return render(request,"goods/goods_list.html")
