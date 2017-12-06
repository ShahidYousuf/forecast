# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.messages import get_messages
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'forecast/home.html', {})

def update(request):
    city = request.POST.get('city')
    if len(city) == 0:
        return redirect('forecast:home')
    else:
        return render(request, 'forecast/update.html', {'city':city})
def detail(request, div, year, month, day, time):
    div = div
    tada = year + '-' + month + '-' + day +' '+ time
    return render(request, 'forecast/detail.html', {"div":div, "tada":tada})
