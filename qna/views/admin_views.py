from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ..models import *
from django.core.paginator import Paginator
from django.db.models import Q
from datetime import datetime
import json
# Create your views here.

@login_required(login_url="account:admin_login")
def admin_qna_list(request):
	seo = {
		'title': "유토빌",
	}

	qna_objs =  QnA.objects.all().order_by('-id')
	
	page        = int(request.GET.get('p', 1))
	pagenator   = Paginator(qna_objs, 12)
	qna_objs = pagenator.get_page(page)

	return render(request, 'admin/qna/qna_list.html',{
		"seo": seo,
		"qna_objs": qna_objs,
	})


@login_required(login_url="account:admin_login")
def admin_qna_detail(request, qna_id):
	seo = {
		'title': "유토빌",
	}

	try:
		qna_obj = QnA.objects.get(pk=qna_id)
	except:
		return redirect('/')

	if request.method == 'POST':
		jsonData = json.loads(request.body)
		answer = jsonData.get('answer')
				
		try:
			qna_obj.answer = answer
			qna_obj.answered_at = datetime.now()
			qna_obj.save()

			result = '200'
			result_text = "답변이 완료되었습니다."
		except:
			result = '201'
			result_text = '알수없는 오류입니다. 다시시도 해주세요.'

		return JsonResponse({
			'result': result, 
			'result_text': result_text
		})
	else:
		return render(request, 'admin/qna/qna_detail.html',{
			"seo":seo,
			"qna_obj": qna_obj
		})

