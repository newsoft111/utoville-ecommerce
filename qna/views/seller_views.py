from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from product.models import *
from django.core.paginator import Paginator
from django.db.models import Q
import json
# Create your views here.

@login_required(login_url="acount:seller_login")
def seller_qna_list(request):
	seo = {
		'title': "유토빌",
	}

	q = Q()
	q &= Q(user = request.user)
	product_list =  Product.objects.filter(q).values_list('id', flat=True).order_by( "-id")
	
	q = Q()
	q &= Q(product__in=product_list)
	qna_list =  ProductQnA.objects.filter(q).order_by('-id')

	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(qna_list, 12)
	qna_list = pagenator.get_page(page)

	return render(request, 'seller/qna/qna_list.html',{
		"seo": seo,
		"qna_list": qna_list,
	})


@login_required(login_url="acount:seller_login")
def seller_qna_detail(request, qna_id):
	seo = {
		'title': "유토빌",
	}

	try:
		qna_obj = ProductQnA.objects.get(pk=qna_id)
	except:
		return redirect('/')

	if request.method == 'POST':
		jsonData = json.loads(request.body)
		answer = jsonData.get('answer')
				
		try:
			qna_obj.answer = answer
			qna_obj.save()

			result = '200'
			result_text = "The answer has been registered"
		except:
			result = '201'
			result_text = 'Unknown error occurred. Please try again.'

		return JsonResponse({
			'result': result, 
			'result_text': result_text
		})
	else:
		return render(request, 'seller/qna/qna_detail.html',{
			"seo":seo,
			"qna_detail": qna_obj
		})


def seller_qna_delete(request):
	seo = {
		'title': "유토빌",
	}
	jsonData = json.loads(request.body)
	qna_id = jsonData.get('qna_id')
	
	try:
		qna_obj = ProductQnA.objects.get(pk=qna_id)
	except:
		return JsonResponse({
			'result': '201', 
			'result_text': 'Unknown error occurred. Please try again.'
		})

	try:
		qna_obj.is_deleted = True
		qna_obj.deleted_at = datetime.now()
		qna_obj.save()

		result = '200'
		result_text = "Refusal has been completed."
	except Exception as e:
		print(e)
		result = '201'
		result_text = 'Unknown error occurred. Please try again.'

	return JsonResponse({
		'result': result, 
		'result_text': result_text
	})

	