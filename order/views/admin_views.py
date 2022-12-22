from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from ..models import *
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url="account:admin_login")
def admin_order_list(request):
	seo = {
		'title': "상품 리스트 - 유토빌",
	}
	q = Q()
	order_item_objs =  OrderItem.objects.filter(q).order_by( "-id")
	
	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(order_item_objs, 12)
	order_item_objs = pagenator.get_page(page)

	return render(request, 'admin/order/order_list.html',{
		"seo":seo,
		'order_item_objs': order_item_objs
	})

@login_required(login_url="account:admin_login")
def admin_order_detail(request, order_item_id):
	seo = {
		'title': "상품주문정보 조회 - 유토빌",
	}
	q = Q()
	q &= Q(pk = order_item_id)

	order_item_obj =  get_object_or_404(OrderItem, q)

	return render(request, 'admin/order/order_detail.html',{
		"seo":seo,
		'order_item_obj': order_item_obj
	})
