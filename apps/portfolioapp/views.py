# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render #, HttpResponse

# Create your views here.
def index(request):
    print '*'*50
    return render(request, 'portfolioapp/index.html')

def testimonials(request):
    print "Where does my heaaaaaaart beeeeeeeeat noooooooooow"
    return render(request, 'portfolioapp/testimonials.html')
    