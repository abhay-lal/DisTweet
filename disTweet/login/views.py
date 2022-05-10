from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request):
    
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username= data.get('username'), password= data.get('password'))
        print(type(user))
        if user is not None:
            auth_login(request, user)
            
        return redirect('/map')

    return render(request, 'login/login.html')


def thanks(request):
    return render(request, 'login/thanks.html')

def registeration(request):
    if request.method == 'POST':
        data = request.POST
        newUser = User.objects.create_user(data.get('username'), password = data.get('password'))
        newUser.save()
        return redirect('/useraccount/thanks')
    
    return render(request, 'login/register.html')