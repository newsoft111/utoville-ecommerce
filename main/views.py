from django.shortcuts import render

# Create your views here.

def index(request):
	seo = {
		'title': "유토빌",
	}
	return render(request, 'main/index.html' ,{"seo":seo})