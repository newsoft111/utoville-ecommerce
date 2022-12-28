from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q, Sum, Avg
from ..models import *
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json, re
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

import urllib
import xlwt
User = get_user_model()

@login_required(login_url="account:admin_login")
def admin_profit_done_list(request):
	now = date.today()
	start_date = now-relativedelta(months=1)
	end_date = now

	if request.GET.get("start_date") is not None and request.GET.get("start_date") != '':
		start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")

	if request.GET.get("end_date") is not None and request.GET.get("end_date") != '':
		end_date = datetime.strptime(request.GET.get("end_date"), "%Y-%m-%d")

	start_date = start_date + timedelta(days=1)
	
	profit_done_objs = Profit.objects.filter(is_done=True)

	profit_done_amount = profit_done_objs.aggregate(Sum('total_profit_amount'))['total_profit_amount__sum']
	if profit_done_amount is None:
		profit_done_amount = 0


	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(profit_done_objs, 10)
	profit_done_objs = pagenator.get_page(page)

	return render(request, 'admin/profit/profit_done_list.html', {
		"profit_done_objs": profit_done_objs,
		'profit_done_amount': profit_done_amount,
	})



@login_required(login_url="account:admin_login")
def admin_profit_done_export(request):
	profit_done_obj = get_object_or_404(Profit, pk=request.GET.get("id"))
	
	q = Q()
	q &= Q(profit=profit_done_obj)

	profit_detail_objs = ProfitDetail.objects.filter(q).order_by(
		'-id'
	).extra(
		select={'created_at_date': 'DATE(created_at)'}
	).values_list(
		'created_at_date', 
		'charge_amount',
		'charge_fee', 
		'shipping_fee',
	)

	file_name = urllib.parse.quote(str(f"{request.user.username} 매출").encode('utf-8'))

	response = HttpResponse(content_type="application/vnd.ms-excel")
	response["Content-Disposition"] = f'attachment;filename*=UTF-8\'\'{file_name}.xls' 
	wb = xlwt.Workbook(encoding='ansi') #encoding은 ansi로 해준다.
	ws = wb.add_sheet('신청자') #시트 추가
	
	row_num = 0
	col_names = ['날짜', '금액', '수수료', '배송비']
	
	#열이름을 첫번째 행에 추가 시켜준다.
	for idx, col_name in enumerate(col_names):
		ws.write(row_num, idx, col_name)
	
	
	
	#유저정보를 한줄씩 작성한다.
	for profit_detail_obj in profit_detail_objs:
		row_num +=1
		for col_num, attr in enumerate(profit_detail_obj):
			ws.write(row_num, col_num, str(attr))
					
	wb.save(response)
	
	return response


@login_required(login_url="account:admin_login")
def admin_profit_expect_list(request):
	profit_expect_objs = Profit.objects.filter(is_done=False)

	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(profit_expect_objs, 10)
	profit_expect_objs = pagenator.get_page(page)


	return render(request, 'admin/profit/profit_expect_list.html', {
		"profit_expect_objs":profit_expect_objs
	})

def admin_profit_expect_change_status(request):
	if request.method == 'POST':
		profit_id = request.POST.get('profit_id')
		status = request.POST.get('status')

		try:
			profit_obj = Profit.objects.get(pk=profit_id)
		except:
			result = {'result': '201', 'result_text': '잘못된 요청입니다.'}
			return JsonResponse(result)

		profit_obj.status = '1'
		profit_obj.save()

		try:
			profit_obj.status = status
			profit_obj.save()
		except:
			result = {'result': '201', 'result_text': '잘못된 요청입니다.'}
			return JsonResponse(result)
		
		result = {'result': '200', 'result_text': profit_obj.get_status_display()}
		return JsonResponse(result)

	else:
		result = {'result': '201', 'result_text': '잘못된 요청입니다.'}
		return JsonResponse(result)


@login_required(login_url="account:admin_login")
def admin_profit_expect_change_memo(request):
	if request.method == 'POST':
		profit_id = request.POST.get('profit_id')
		memo = request.POST.get('memo')

		try:
			profit_obj = Profit.objects.get(pk=profit_id)
		except:
			result = {'result': '201', 'result_text': '잘못된 요청입니다.'}
			return JsonResponse(result)

		try:
			profit_obj.memo = memo
			profit_obj.save()

		except:
			result = {'result': '201', 'result_text': '잘못된 요청입니다.'}
			return JsonResponse(result)

		result = {'result': '200', 'result_text': '처리가 완료되었습니다.'}
		return JsonResponse(result)
		
	else:
		result = {'result': '201', 'result_text': '잘못된 요청입니다.'}
		return JsonResponse(result)


@login_required(login_url="account:admin_login")
def admin_profit_expect_detail(request, profit_id):
	profit_expect_obj = get_object_or_404(Profit, pk=profit_id)

	q = Q()
	q &= Q(profit=profit_expect_obj.pk)

	profit_detail_objs = ProfitDetail.objects.filter(q).order_by('-id')

	return render(request, 'admin/profit/profit_expect_detail.html', {
		"profit_detail_objs":profit_detail_objs
	})