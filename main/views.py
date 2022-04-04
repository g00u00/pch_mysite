import datetime
from django.shortcuts import render
from django.http import HttpResponse
#from django.urls import reverse

# def index(request):
#     return HttpResponse("Hello, world. You'reat the polls index.")

def index(request):
    return render(request, 'main/index.html')

# def index(request):
#     name_main="index"
#     redirect_url=reverse ('index', args=(name_main))
#     return render(request, redirect_url)

def main(request):
    list_main= (1,3)
    print (list_main)
    context ={'list_main': list_main }
    return render(request, 'main/main.html', context)


# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


# def current_datetime(request):
#     datetime_now = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(datetime_now)
def datetime_nov(request):
    now=list()
    now.append(datetime.datetime.now())
    print('datetime.datetime.now(): ', now)
    list_main= now
    print (list_main)
    context ={'list_main': list_main }
    return render(request, 'main/datetime_now.html', context)

