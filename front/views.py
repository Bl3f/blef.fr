from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime


def home(request):
    home_context = {
        'header_title': 'blef',
        'nav_menu': ['home', 'experience', 'resume', 'contact'],
    }
    return render(request, "front/home.html", home_context)