from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You'reat the polls index.")
def index(request):
    return render(request, 'main/index.html')

def abc(request):
    return HttpResponse("abc")