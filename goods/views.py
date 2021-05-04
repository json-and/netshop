from django.shortcuts import render,HttpResponse
from django.db import models
from django.views import View
# Create your views here.
from goods import models
from goods.models import *

#
# def index(request,cid=1):
#      cid=int(cid)
#      # 查询所有类别信息
#      categorys=Category.objects.all().order_by('id')
#      print(Category.cname)
#      #查询当前类别下的所有商品信息
#      goodsList=Goods.objects.filter(category_id=2).order_by('id')
#      return render(request,"index.html",{'categorys':categorys,'goodsList':'goodsList','currentCid':cid})
class IndexView(View):
    def get(self,request,cid=1):
         categorys = Category.objects.all().order_by('id')

         # 查询当前类别下的所有商品信息
         goodsList = Goods.objects.filter(category_id=cid).order_by('id')

         return render(request, 'index.html',
                       {'categorys': categorys, 'goodsList': goodsList, 'currentCid': cid
                        })

