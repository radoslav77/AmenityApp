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
from datetime import timedelta

from .forms import *


#global variebles
time = datetime.datetime.now()
TODAY = time.strftime('%Y'+'-'+'%m'+'-'+'%d')
DATA = InputAmenity.objects.all()

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

    print(TODAY)
    today_arr = []
    for d in DATA:
        if d.arrival_date == TODAY:
            today_arr.append(d)
    return render(request, 'calc/today.html', {
        'data': today_arr
    })


def archive(request):
    arch = []
    print()
    for i in DATA:

        #arr = i.arrival_date.strftime('%d'+'/'+'%m'+'/'+'%Y')
        if i.arrival_date < TODAY:
            arch.append(i)

    print(arch)
    return render(request, 'calc/archive.html', {
        'data': arch
    })


def tomorrow(request):
    t = datetime.datetime.now() + timedelta(days=1)
    x = t.strftime('%Y'+'/'+'%m'+'/'+'%d')
    # print(datetime.datetime.now() + timedelta(days=1)) in timedelta increase arrgument to add day to realtime
    tom = []
    for i in DATA:

        if i.arrival_date == x:
            tom.append(i)

    return render(request, 'calc/archive.html', {
        'data': tom
    })
