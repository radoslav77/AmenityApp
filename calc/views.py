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

# API database


def json_data(request):

    JSON_data = []

    for i in DATA:
        JSON_data.append({
            'big_id': i.big_id,
            'name': i.name,
            'arrival_date': i.arrival_date,
            # 'month': i.arrival_date[5:7]
            # 'data': i.date
        })

    return HttpResponse(json.dumps(JSON_data), content_type="application/json")


def archive(request):
    arch = []
    mon = set()
    date = []
    for i in DATA:
        #month = i.arrival_date

        # print(month[5:7])
        #arr = i.arrival_date.strftime('%d'+'/'+'%m'+'/'+'%Y')
        if i.arrival_date < TODAY:
            arch.append(i)
    for m in arch:
        mon.add(m.arrival_date[5:7])
        date.append(m.arrival_date)
    # month = json.dumps(mon), content_type="application/json"
    print(mon)
    return render(request, 'calc/archive.html', {
        'data': arch,
        'month': mon,
        'dates': date
    })


def arch_month(request, month):
    print(month)

    return render(request, 'calc/arch-month.html')


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


def total(request):
    lrg_fruit = []
    mid_fruit = []
    small_fruit = []

    for i in DATA:
        if i.fruit_amenity == 'Large fruit':
            lrg_fruit.append(i)
        elif i.fruit_amenity == 'Midium fruit':
            mid_fruit.append(i)
        else:
            small_fruit.append(i)
