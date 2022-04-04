from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('datetime_nov/', views.datetime_nov, name='datetime_nov'),
]
