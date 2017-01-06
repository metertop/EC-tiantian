#coding:utf-8
from django.shortcuts import render
from models import *

#首页
def index(request):
    goodsList = []
    typeInfo = TypeInfo.objects.all()
    for type in typeInfo:
        list = GoodsInfo.objects.filter(gtype_id=type.id)[:4]
        # 列表不为空进行添加
        if list:
            goodsList.append(list)

    context = {'list': goodsList}
    return render(request,"goods/index_shopping.html",context)

# 详情
def detail(request,id):
    id = int(id)
    list = GoodsInfo.objects.get(id=id)
    # 通过过滤取出对应的商品分类且是新品的商品
    list1 = GoodsInfo.objects.filter(gnews='news',gtype=list.gtype)
    context = {'goods':list,'list1':list1}
    return render(request,"goods/base_detail.html",context)

# 列表页
def list(request,id):
    list = GoodsInfo.objects.filter(gtype_id=id)
    list1 = GoodsInfo.objects.filter(gtype_id=id,gnews='news')
    context = {'list':list,'list1':list1}
    print list1
    return render(request,"goods/goods_list.html",context)
