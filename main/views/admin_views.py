from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="account:admin_login")
def admin_index(request):
	seo = {
		'title': "유토빌",
	}
	return render(request, 'admin/main/index.html',{"seo":seo})