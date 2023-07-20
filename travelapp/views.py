from django.http import HttpResponse
from django.shortcuts import render
from . models import Place

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request, "index.html",{'result':obj})









#
# def add(request):
#     x = int(request.GET['num1'])  # num1 is the name of field in home.html
#     y = int(request.GET['num2'])
#     res = x + y
#     mul = x * y
#     div = x / y
#     sub = x - y
#     return render(request, "about.html", {'result': res, 'multi': mul, 'divi': div, 'subt': sub})

# def about(request):
#     return render(request, "about.html")
#
#
# def contact(request):
#     return render(request, "contact.html")
