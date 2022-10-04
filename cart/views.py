from django.shortcuts import render

# Create your views here.
def cart_list(request):
   seo = {
      'title': "장바구니 - 유토빌",
   }

   return render(request, 'cart/cart_list.html' ,{
      "seo":seo,
   })