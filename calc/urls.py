
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
    path('arch-month/<str:month>', views.arch_month, name='arch_month'),
    path('months/<str:months>', views.months, name='months'),
    path('total/<str:months>', views.total, name='total'),

    # API
    path('json_data', views.json_data, name='json_data')

]
