from django.shortcuts import render

from django.views import View
# Create your views here.
from goods import models
from goods.models import *


def index(request,cid=2):
     cid=int(cid)
     # 查询所有类别信息
     cate_list=Category.objects.all().order_by('id')
     #查询当前类别下的所有商品信息
     good_list=Goods.objects.filter(category_id=2).order_by('id')
     return render(request,"index.html",{'categorys':cate_list,'goodslist':'good_list','currentcid':cid})