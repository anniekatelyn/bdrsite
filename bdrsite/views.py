# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world")
    return render(request,'bdrsite/index.html')