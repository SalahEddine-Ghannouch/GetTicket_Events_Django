from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.contrib.auth.models import User
from events.models import EventCategory, Event
from .forms import LoginForm

@login_required(login_url='login_admin')
def dashboard(request):
    user = User.objects.count()
    event_ctg = EventCategory.objects.count()
    event = Event.objects.count()
    complete_event = Event.objects.filter(status='completed').count()
    events = Event.objects.all()  #!commented
    context = {
        'user': user,
        'event_ctg': event_ctg,
        'event': event,
        'complete_event': complete_event,
        'events': events
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login_admin')
def dashboard_organ(request):
    # user = request.user
    event_ctg = EventCategory.objects.count()
    event = Event.objects.filter(created_user_id=request.user.id).count()
    complete_event = Event.objects.filter(created_user_id=request.user.id, status='completed').count()
    events = Event.objects.filter(created_user_id=request.user.id)    #!added

    count_noti = Event.objects.filter(created_user_id=request.user.id, status='active').count()
    noti_events = Event.objects.filter(created_user_id=request.user.id, status='active')
    event_names = [event for event in noti_events]

    context = {
        'event_ctg': event_ctg,
        'event': event,
        'complete_event': complete_event,
        'events': events,
        'count_noti':count_noti,
        'event_names':event_names,
        'noti_events':noti_events
    }
    return render(request, 'dashboard_organ.html', context)


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_staff:
                    # login(request, user)
                    return redirect('dashboard_organ')
                else:
                    login(request, user)
                    return redirect('dashboard')
                    
    context = {
        'form': forms
    }
    return render(request, 'login_admin.html', context)

def logut_page(request):
    logout(request)
    return redirect('/')