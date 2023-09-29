from django.shortcuts import render
from django.views import generic
from .models import Recipe


def check_the_base(request):
    return render(request, 'base.html')

