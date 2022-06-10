from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'home/index.html')