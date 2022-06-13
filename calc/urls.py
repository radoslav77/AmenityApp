
from django import views
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('input', views.update, name='update'),
    path('today', views.daily, name='daily'),
    path('archive', views.archive, name='archive'),
    path('tommorow', views.tomorrow, name='tomorrow'),

]
