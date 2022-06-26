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


# global variebles
time = datetime.datetime.now()
TODAY = time.strftime('%Y'+'-'+'%m'+'-'+'%d')
DATA = InputAmenity.objects.all()
YearMounts = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
              '07': 'July', '08': 'Auguest', '09': 'September', '10': 'Octouber', '11': 'November', '12': 'December'}

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
    return redirect('calc:index')


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
        for key in YearMounts:
            if i.arrival_date[5:7] == key:
                mon = YearMounts[key]
                # print(mon)
        JSON_data.append({
            'big_id': i.big_id,
            'name': i.name,
            'arrival_date': i.arrival_date,
            'month': mon
            # 'data': i.date
        })

    return HttpResponse(json.dumps(JSON_data), content_type="application/json")


def archive(request):
    arch = []
    date = []
    months = set()
    for i in DATA:
        '''
        for key in YearMounts:
            if i.arrival_date[5:7] == key:
                months.add(YearMounts[key])
                month = YearMounts[key]
        '''
        date.append({
            'date': i.arrival_date,
            'month': i.month
        })

        # arr = i.arrival_date.strftime('%d'+'/'+'%m'+'/'+'%Y')
        if i.arrival_date < TODAY:
            arch.append(i)

    return render(request, 'calc/archive.html', {
        'data': arch,
        'dates': date,
        'months': months,
    })


def months(request, months):
    cur_month = []
    for i in DATA:
        if i.month == months:
            cur_month.append(i)
    return render(request, 'calc/arch-month.html', {
        'data': cur_month
    })


def arch_month(request, month):

    data = InputAmenity.objects.filter(arrival_date=month)
    for i in data:
        print(i)

    return render(request, 'calc/arch-month.html', {
        'data': data
    })


def tomorrow(request):
    t = datetime.datetime.now() + timedelta(days=1)
    x = t.strftime('%Y'+'-'+'%m'+'-'+'%d')
    # print(datetime.datetime.now() + timedelta(days=1)) in timedelta increase arrgument to add day to realtime
    tom = []
    for i in DATA:

        if i.arrival_date == x:
            tom.append(i)
    print(x)
    return render(request, 'calc/archive.html', {
        'data': tom
    })


def total(request, months):
    lrg_fruit = []
    mid_fruit = []
    small_fruit = []

    for i in DATA:
        if i.month == months:
            if i.fruit_amenity == 'Large fruit':
                lrg_fruit.append(i.fruit_amenity)
            elif i.fruit_amenity == 'Midium fruit':
                mid_fruit.append(i.fruit_amenity)
            else:
                small_fruit.append(i.fruit_amenity)

    return render(request, 'calc/total.html', {
        'fruits': lrg_fruit,
        'sm_fruits': small_fruit,
        'mid_fruits': mid_fruit
    })
