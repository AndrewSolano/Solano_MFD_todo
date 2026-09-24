from datetime import datetime
from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm

def home(request):
    now = datetime.now()
    date_str = now.strftime('%B %d, %Y')

    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all()
            context = {'all_items': all_items, 'date_today': date_str}
            return render(request, 'home.html', context)
    else:
        all_items = List.objects.all()
        context = {'all_items': all_items, 'date_today': date_str}
        return render(request, 'home.html', context)

def about(request):
    context = {'myname': 'bob'}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    return redirect('home')

def strike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def unstrike(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')