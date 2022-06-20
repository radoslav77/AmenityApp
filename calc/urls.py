
from django import views
from django.urls import path, include
from . import views

app_name = "calc"

urlpatterns = [
    path('', views.index, name='index'),
    path('input', views.update, name='update'),
    path('today', views.daily, name='daily'),
    path('archive', views.archive, name='archive'),
    path('tommorow', views.tomorrow, name='tomorrow'),
    path('arch-month/<int:month>', views.arch_month, name='arch_month')

]
