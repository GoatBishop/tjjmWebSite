# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def mainIndex(request):
    html = "<h1>Hello</h1>"
    return HttpResponse(html)

