from calendar import month
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
              '07': 'July', '08': 'Auguest', '09': 'September', '10': 'Octomber', '11': 'November', '12': 'December'}
DATA_LONG_STAY = LongStay.objects.all()

FRUIT = ['Large fruit', 'Midium fruit','Small fruit','Presidential']
DRINK = ['White wine','Red wine','Champagne', 'Negroni', 'Water']
TURN_DOWN = ['Florentine', 'Macaroons', 'Pistachio Finnacier','Madleines', 'Flapjack','Lemon cake']
DESSERT = ['Chocolate truffle', 'Macaroons 4pcs', 'Macaroons 8pcs', 'Baklava', 'Maamul', 'Arab amenity']


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
        'data': today_arr,
        'today':TODAY
    })

# API database


def json_data(request):
# need to update jaso API with all data from the database
    JSON_data = []

    for i in DATA:
        for key in YearMounts:
            if i.arrival_date[5:7] == key:
                mon = YearMounts[key]
        #arrival = datetime.datetime.strftime(i.arrival_date, '%d'+'/'+'%m'+'/'+'%Y')
        #print(arrival)
        
        JSON_data.append({
            'big_id': i.big_id,
            'name': i.name,
            'arrival_date': i.arrival_date,
            'month': mon,
            'membership': i.membership,
            'num_fruit': i.num_of_fruit,
            'fruit_amenity': i.fruit_amenity,
            'num_drink': i.num_of_drink,
            'drink_amenity': i.drink_amenity,
            'num_dessrt': i.num_of_dessert,
            'dessert_amenity': i.dessert_amenity,
            'birthday_amenity': i.birthday_amenity,
            'date': time.strftime('%Y'+'-'+'%m'+'-'+'%d')
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
        months.add(i)
        # arr = i.arrival_date.strftime('%d'+'/'+'%m'+'/'+'%Y')
        if i.arrival_date < TODAY:
            arch.append(i)
    #print(months)
    return render(request, 'calc/archive.html', {
        'data': arch,
        'dates': date,
        'months': months,
    })


def months(request, months):
    cur_month = []
   
    for i in DATA:
        for key in YearMounts:
            if i.month == YearMounts[key]:
                print(i)
        
        if i.month == months:
            cur_month.append(i)
    
    print(i.month, '+>', months)       
    return render(request, 'calc/arch-month.html', {
        'data': cur_month,
        'month': months
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
    print(tom)
    return render(request, 'calc/tomorrow.html', {
        'data': tom,
        'tomorrow': x
    })

def dayaftertomorrow(request):
    t = datetime.datetime.now() + timedelta(days=2)
    x = t.strftime('%Y'+'-'+'%m'+'-'+'%d')
    # print(datetime.datetime.now() + timedelta(days=1)) in timedelta increase arrgument to add day to realtime
    tom = []
    for i in DATA:

        if i.arrival_date == x:
            tom.append(i)
    print(tom)
    return render(request, 'calc/tomorrow.html', {
        'data': tom,
        'tomorrow': x
    })


def total(request, months):
    lrg_fruit = []
    mid_fruit = []
    small_fruit = []
    long_stay = []

    fruit = []
    drink = []
    pastry = []
    data = InputAmenity.objects.filter(month=months)

    for i in DATA:
        if i.month == months:
            if i.fruit_amenity == 'Large fruit':
                lrg_fruit.append(i.fruit_amenity)
            elif i.fruit_amenity == 'Midium fruit':
                mid_fruit.append(i.fruit_amenity)
            else:
                small_fruit.append(i.fruit_amenity)
            for e in FRUIT:
                if i.fruit_amenity == e:
                    fruit.append(e)
            for d in DRINK:
                if i.drink_amenity == d:
                    drink.append(d)
            for s in DESSERT:
                if i.dessert_amenity == s:
                    pastry.append(s)
                    print(s)
    for j in DATA_LONG_STAY:
        if j.month == months:
            long_stay.append(j)
    #print(DATA_LONG_STAY)
    #print(lrg_fruit, '-', mid_fruit, '-', small_fruit)
    return render(request, 'calc/total.html', {
        'fruits': len(lrg_fruit),
        'sm_fruits': len(small_fruit),
        'mid_fruits': len(mid_fruit),
        'longstay': len(long_stay),
        'month': months,
        'data': data
    })
#need more work 
def uptodate(request, months):
    uptodate_data = []
    for d in DATA:
        t = datetime.datetime.now() + timedelta(days=1)
        x = t.strftime('%Y'+'-'+'%m'+'-'+'%d')
        #print(t, '-', x)
        if d.arrival_date == x:
            if d.month == months:
                print(d.arrival_date)
        elif d.arrival_date != x:
            if d.month == months:
                uptodate_data.append(d)
    print(uptodate_data)
    return render(request, 'calc/total.html',
    {
        'uptodate': uptodate_data,
        'month': months
    })

    def user(request):
        pass

    def login(request):
        pass 