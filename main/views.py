from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	seo = {
		'title': "유토빌",
	}
	return redirect("product:detail")