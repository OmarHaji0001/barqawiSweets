from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.conf import settings


def mainPage(request):
    return render(request, 'pages/main.html')
