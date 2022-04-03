from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('mainf/ ', views.mainf, name='mainf'),
    path('current_datetime/', views.current_datetime, name='current_datetime'),

]
