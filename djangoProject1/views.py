# from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello World")
