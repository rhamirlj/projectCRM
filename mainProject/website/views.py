from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    #check to see if logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
    
    return render(request,'home.html',{})



def logout_user(request):
    pass