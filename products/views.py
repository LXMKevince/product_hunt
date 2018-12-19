from django.shortcuts import render

# Create your views here.


def product_list(requset):
    return render(requset, 'product_list.html')
