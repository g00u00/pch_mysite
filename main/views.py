from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
import datetime

# def index(request):
#     return HttpResponse("Hello, world. You'reat the polls index.")

def index(request):
    return render(request, 'main/index.html')

# def index(request):
#     name_main="index"
#     redirect_url=reverse ('index', args=(name_main))
#     return render(request, redirect_url)


def mainf(request):
    dict_main= {"i0",1}
    return render(request, 'mainf.html')


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


# def current_datetime(request):
#     datetime_now = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(datetime_now)
def current_datetime(request):
    now = datetime.datetime.now()
    print('datetime.datetime.now(): ', now)
    return render(request, 'main/datetime_now.html', now)

