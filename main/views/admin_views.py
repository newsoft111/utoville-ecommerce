from django.shortcuts import render, redirect

# Create your views here.

def admin_index(request):
	seo = {
		'title': "유토빌",
	}
	return render(request, 'admin/main/index.html',{"seo":seo})