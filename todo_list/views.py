
from django.shortcuts import render
from datetime import datetime
from django. shortcuts import render


def home(request):
    now = datetime.nowO
    return render(request, 'home.html', {})
def about(request):
    context = {'myname' : 'bob'}
    return render(request, 'about.html', context)
def about(request):
    return render(request, 'about.html', {})