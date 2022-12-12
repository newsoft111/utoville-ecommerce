from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q, Sum
from ..models import *
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json, re
import urllib
import xlwt
User = get_user_model()

def profit_list(request):
	profit_objs = Profit.objects.filter(profit_done=None)
	profit_amount = profit_objs.aggregate(Sum('profit_amount'))['profit_amount__sum']
	if profit_amount is None:
		profit_amount = 0

	now = date.today()
	start_date = now-relativedelta(months=1)
	end_date = now

	if request.GET.get("start_date") is not None and request.GET.get("start_date") != '':
		start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")

	if request.GET.get("end_date") is not None and request.GET.get("end_date") != '':
		end_date = datetime.strptime(request.GET.get("end_date"), "%Y-%m-%d")

	start_date = start_date + timedelta(days=1)
	
	profit_done_objs = ProfitDone.objects.filter(created_at__range=[start_date, end_date])

	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(profit_done_objs, 10)
	profit_done_objs = pagenator.get_page(page)

	return render(request, 'profit/profit_list.html', {
		"profit_objs": profit_objs,
		'profit_amount': profit_amount,
		'profit_done_objs': profit_done_objs
	})



@login_required(login_url="account:login")
def profit_export(request):
	profit_done_obj = get_object_or_404(ProfitDone, pk=request.GET.get("id"))
	
	q = Q()
	q &= Q(profit_done=profit_done_obj)

	profit_objs = Profit.objects.filter(q).order_by(
		'-id'
	).extra(
		select={'created_at_date': 'DATE(created_at)'}
	).values_list(
		'created_at_date', 
		'charge_amount',
		'payment_fee', 
		'profit_amount',
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
	for profit_obj in profit_objs:
		row_num +=1
		for col_num, attr in enumerate(profit_obj):
			ws.write(row_num, col_num, str(attr))
					
	wb.save(response)
	
	return response