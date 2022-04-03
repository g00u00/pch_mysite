from django.urls import path
from . import views

app_name = "pools"
urlpatterns = [
    path('', views.index, name='index'),
    path('polls/', views.polls, name='polls'),

]
