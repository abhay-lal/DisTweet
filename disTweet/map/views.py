from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def mapy(request):
    if request.method == 'POST':
        logout(request)
        return redirect(request, '/')
    return render(request, 'map/map.html')