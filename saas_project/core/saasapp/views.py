from django.shortcuts import render
from .models import Plan


def home(request):
   return render(request, 'home.html')


def pricing(request):
    plans = Plan.objects.all()
    return render(request, 'pricing.html', {'plans': plans})