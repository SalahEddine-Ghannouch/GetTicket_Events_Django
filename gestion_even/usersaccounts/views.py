from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login,update_session_auth_hash
from events.models import Payments, Event
from django.db.models import OuterRef
from django.http import HttpResponseRedirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists() :
                messages.info(request, 'Username already exists ')
                form_data = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email,
                }
                return render(request, 'register.html', {'form_data': form_data})
            elif User.objects.filter(email=email).exists() :
                 messages.info(request, 'Email already exists ')
                 form_data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'username': username,
                    'email': email,
                    }
                 return render(request, 'register.html', {'form_data': form_data})
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                login(request, user)
                return redirect('/')
        else:
             messages.info(request, 'Password not matching')
             form_data = {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email,
                }
             return render(request, 'register.html', {'form_data': form_data})
    else:
        return render(request,'register.html')
    

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        mypassword = request.POST['password']
        try:
            username = User.objects.get(email=email)
            user = auth.authenticate(username= username, password=mypassword)
            if user is not None:
                auth.login(request, user)
                login(request, user)
                # response = render(request, 'index.html')
                # response.set_cookie('username',username)
                # response.set_cookie('user',user)
                return redirect('/')
            else:
                messages.info(request, 'Incorrect password')
                form_data = {
                'email': email,
                }
                return render(request, 'login.html', {'form_data' : form_data})
        except User.DoesNotExist:
            messages.info(request,'Incorrect email')
            form_data = {
                'email': email,
                }
            return render(request, 'login.html', {'form_data' : form_data})

    else:
        return render(request,'login.html')
    

def logout_user(request):
    auth.logout(request)
    response = redirect('/')
    # response.delete_cookie('username')
    # response.delete_cookie('user')
    return response



def profile_user(request):
    if request.user.is_authenticated:
        current_user = request.user
        oldusername = current_user.username
        oldemail = current_user.email
        pays = Payments.objects.filter(username=str(current_user))
        events = Event.objects.all()

        joined_data = {}
        for payment in pays:
            event = events.filter(name=payment.eventName).first()
            if event:
                joined_data[payment] = event
        # joined_data = {payment: event for payment, event in joined_data.items() if event}

        if request.method == 'POST':
            current_user.first_name = request.POST.get('first_name')
            current_user.last_name = request.POST.get('last_name')
            current_user.username = request.POST.get('username')
            current_user.email = request.POST.get('email')

            new_password = request.POST.get('password1')
            new_password2 = request.POST.get('password2')
            if(new_password == new_password2):
                if User.objects.filter(username=request.POST.get('username')).exists() and current_user.username != oldusername:
                    messages.info(request, 'Username already exists')

                    return render(request, 'profile.html',{'joined_data':joined_data})
                else:
                    if User.objects.filter(email=request.POST.get('email')).exists() and current_user.email != oldemail:
                        messages.info(request, 'Email already exists')

                        return render(request, 'profile.html',{'joined_data':joined_data})
                    else:
                        if new_password:
                            current_user.set_password(new_password)
                            update_session_auth_hash(request, current_user)
                        current_user.save()

                        return render(request, 'profile.html',{'joined_data':joined_data})
            else:
                messages.info(request, 'Password not matching')

                return render(request, 'profile.html',{'joined_data':joined_data})
        else:

            return render(request, 'profile.html',{'joined_data':joined_data})
    else:
        messages.info(request, 'You need to SignIn to access the Profil page!')
        return render(request, 'register.html')
    