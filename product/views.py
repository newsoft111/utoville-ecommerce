from itertools import product
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *
from category.models import *
from collections import defaultdict
import json


# Create your views here.
def product_list(request):
	seo = {
		'title': "상품 리스트 - 유토빌",
	}

	q = Q()
	if request.GET.get("category1"): #카테고리1 필터
		q &= Q(category_first = int(request.GET.get("category1")))
	if request.GET.get("category2"): #카테고리2 필터
		q &= Q(category_second = int(request.GET.get("category2")))
	if request.GET.get("category3"): #카테고리3 필터
		q &= Q(category_third = int(request.GET.get("category3")))
	if request.GET.get("area"): #지역 필터
		q &= Q(productarea__area = request.GET.get("area"))
	if request.GET.get("keyword"): #검색 필터
		q &= Q(product_name__icontains = request.GET.get("keyword"))

	ordering_list = ["rating_count", "rating", "id", "price", "-price"]
	if request.GET.get("sort") in ordering_list:
		ordering = request.GET.get("sort")
	else:
		ordering = "-id"
	product_list =  Product.objects.filter(q).order_by(ordering)

	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(product_list, 12)
	product_list = pagenator.get_page(page)

	return render(request, 'product/product_list.html' ,{
		"seo":seo,
		"product_list":product_list,
	})


def product_detail(request, product_id):
	seo = {
		'title': "상품 디테일 - 유토빌",
	}

	product_detail = get_object_or_404(Product, pk=product_id)

	q = Q()
	q &= Q(product = product_id)

	variant_list = ProductVariant.objects.filter(q).values_list('id', flat=True).order_by( "-id")
	
	variant_value_list = ProductVariantValue.objects.filter(variant__in=variant_list)

	variant_data = {}
	for variant_value in variant_value_list:
		key = variant_value.variant.variant
		if key not in variant_data:
			variant_data[key] = []

		variant_data[key].append({
			'id':variant_value.pk, 
			'value':variant_value.value, 
			'price':str(variant_value.price)
		})
	
	print(variant_data)
	q = Q()
	q &= Q(product = product_id)
	q &= ~Q(answer = None)
	q &= ~Q(answer = '')
	product_qna_objs = ProductQnA.objects.filter(q).order_by("-id")

	return render(request, 'product/product_detail.html' ,{
		"seo":seo,
		"product_detail": product_detail,
		"product_qna_objs": product_qna_objs,
		'variant_data': variant_data
	})


def product_qna_question(request):
	if request.method == 'POST':
		question = request.POST.get("question")
		product_id = request.POST.get("product_id")

		try:
			product_obj = Product.objects.get(pk=product_id)
		except:
			result = {
				'result': "201", 
				'result_text': '알수없는 오류입니다. 다시시도 해주세요.'
			}
			return JsonResponse(result)

		try:
			product_qna = ProductQnA()
			product_qna.question = question
			product_qna.user = request.user
			product_qna.product = product_obj
			product_qna.save()

			result = '200'
			result_text = "등록이 완료되었습니다."
		except Exception as e:
			print(e)
			result = '201'
			result_text = '알수없는 오류입니다. 다시시도 해주세요.'

		result = {'result': result, 'result_text': result_text}
		return JsonResponse(result)
	else:
		return redirect("product:list")



def product_review_write(request):
	review = request.POST.get("review")
	rating = request.POST.get("rating")
	product_id = request.POST.get("review_product_id")
	images = request.FILES.getlist('images')

	try:
		product_obj = Product.objects.get(pk=product_id)
	except:
		result = {
			'result': "201", 
			'result_text': '알수없는 오류입니다. 다시시도 해주세요.'
		}
		return JsonResponse(result)

	try:
		product_review_obj= ProductReview()
		product_review_obj.user = request.user
		product_review_obj.product = product_obj
		product_review_obj.review = review
		product_review_obj.rating = rating
		product_review_obj.save()

		for image in images:
			product_review_image_obj = ProductReviewImage()
			product_review_image_obj.product_review = product_review_obj
			product_review_image_obj.image = image
			product_review_image_obj.save()

		result = '200'
		result_text = "등록이 완료되었습니다."
	except Exception as e:
		result = '201'
		result_text = '알수없는 오류입니다. 다시시도 해주세요.'

	result = {'result': result, 'result_text': result_text}
	return JsonResponse(result)
