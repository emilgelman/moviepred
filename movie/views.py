from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login2
from django.shortcuts import render, redirect

from movie.forms import SignUpForm


def index(request):
    return render(request, 'home.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print (form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            print (username);
            print (raw_password);
            user = authenticate(username=username, password=raw_password)
            login2(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def new(request):
    return render(request,'new.html')

def manage(request):
    return render(request,'manage.html')

def details(request):
    tes = request.GET.get("movie")
    print(tes)
    return render(request, 'details.html')

