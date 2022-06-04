from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.models import update_last_login
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse
from django.http import JsonResponse
import json
import datetime

from .forms import *

# Create your views here.


def index(request):

    return render(request, 'calc/index.html', {
        'form': InputData()
    })


def update(request):
    if request.method == 'POST':
        form = InputData(request.POST, request.FILES)
        if form.is_valid:
            data = form.save(commit=False)
            print(data)
            data.save()
    return redirect('index')


def daily(request):

    time = datetime.datetime.now()
    today = time.strftime('%d'+'/'+'%m'+'/'+'%Y')
    data = InputAmenity.objects.all()

    print(time.strftime('%d'+'/'+'%m'+'/'+'%Y'))
    today_arr = []
    for d in data:
        if d.arrival_date == today:
            today_arr.append(d)
    return render(request, 'calc/today.html', {
        'data': today_arr
    })
