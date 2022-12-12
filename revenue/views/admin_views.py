from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import *
from django.db.models import Q, Sum
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.core.paginator import Paginator
import urllib
import xlwt
from django.http import JsonResponse, HttpResponse

@login_required(login_url="account:login")
def revenue_list(request):
	now = date.today()
	start_date = now-relativedelta(months=1)
	end_date = now

	if request.GET.get("start_date") is not None and request.GET.get("start_date") != '':
		start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")

	if request.GET.get("end_date") is not None and request.GET.get("end_date") != '':
		end_date = datetime.strptime(request.GET.get("end_date"), "%Y-%m-%d")

	start_date = start_date + timedelta(days=1)

	revenue_admin_objs = RevenueAdmin.objects.filter(date__range = [start_date, end_date])

	payment_amount = revenue_admin_objs.aggregate(Sum('payment_amount'))['payment_amount__sum']
	if payment_amount is None:
		payment_amount = 0

	refund_amount = revenue_admin_objs.aggregate(Sum('refund_amount'))['refund_amount__sum']
	if refund_amount is None:
		refund_amount = 0

	total_payment = payment_amount-refund_amount


	temp = { po.date.strftime("%Y-%m-%d"): {"payment_amount": po.payment_amount, "refunt_amount": po.payment_amount, "order_count":po.order_count} for po in revenue_admin_objs }
	result = []

	for dy in range(0, (end_date-(start_date-timedelta(days=1))).days):
		loop_date = (end_date-timedelta(days=dy)).strftime("%Y-%m-%d")
		result.append({
			'date': loop_date,
			'payment_amount': temp[loop_date]['payment_amount'] if loop_date in temp else 0,
			'refunt_amount': temp[loop_date]['refunt_amount'] if loop_date in temp else 0,
			'order_count': temp[loop_date]['order_count'] if loop_date in temp else 0,
		})

	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(result, 10)
	result = pagenator.get_page(page)

	return render(request, 'revenue/revenue_list.html', {
		"revenue_admin_objs": result,
		'payment_amount': payment_amount,
		'refund_amount': refund_amount,
		'total_payment': total_payment
	})


@login_required(login_url="account:login")
def revenue_export(request):
	now = date.today()
	start_date = now-relativedelta(months=1)
	end_date = now

	if request.GET.get("start_date") is not None and request.GET.get("start_date") != '':
		start_date = datetime.strptime(request.GET.get("start_date"), "%Y-%m-%d")

	if request.GET.get("end_date") is not None and request.GET.get("end_date") != '':
		end_date = datetime.strptime(request.GET.get("end_date"), "%Y-%m-%d")

	start_date = start_date + timedelta(days=1)

	revenue_admin_objs = RevenueAdmin.objects.filter(date__range = [start_date, end_date])

	payment_amount = revenue_admin_objs.aggregate(Sum('payment_amount'))['payment_amount__sum']
	if payment_amount is None:
		payment_amount = 0

	refund_amount = revenue_admin_objs.aggregate(Sum('refund_amount'))['refund_amount__sum']
	if refund_amount is None:
		refund_amount = 0

	total_payment = payment_amount-refund_amount


	temp = { po.date.strftime("%Y-%m-%d"): {"payment_amount": po.payment_amount, "refunt_amount": po.payment_amount, "order_count":po.order_count} for po in revenue_admin_objs }
	result_datas = []

	for dy in range(0, (end_date-(start_date-timedelta(days=1))).days):
		loop_date = (end_date-timedelta(days=dy)).strftime("%Y-%m-%d")
		result_datas.append({
			'date': loop_date,
			'payment_amount': temp[loop_date]['payment_amount'] if loop_date in temp else 0,
			'refunt_amount': temp[loop_date]['refunt_amount'] if loop_date in temp else 0,
			'order_count': temp[loop_date]['order_count'] if loop_date in temp else 0,
		})

	file_name = urllib.parse.quote(str(f"{request.user.username} 매출").encode('utf-8'))

	response = HttpResponse(content_type="application/vnd.ms-excel")
	response["Content-Disposition"] = f'attachment;filename*=UTF-8\'\'{file_name}.xls' 
	wb = xlwt.Workbook(encoding='ansi') #encoding은 ansi로 해준다.
	ws = wb.add_sheet('신청자') #시트 추가
	
	row_num = 0
	col_names = ['날짜', '결제금액', '환불금액', '주문수']
	
	#열이름을 첫번째 행에 추가 시켜준다.
	for idx, col_name in enumerate(col_names):
		ws.write(row_num, idx, col_name)
			
	
	#유저정보를 한줄씩 작성한다.
	for result_data in result_datas:
		row_num +=1
		print(type(result_data))
		for col_num, attr in enumerate(result_data.values()):
			print(attr)
			ws.write(row_num, col_num, attr)
					
	wb.save(response)
	
	return response