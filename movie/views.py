from django.contrib.auth import authenticate
from django.contrib.auth import login as login2
from django.shortcuts import render, redirect

from movie.forms import SignUpForm

def index(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login2(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def new(request):
    return render(request, 'new.html')

def manage(request):
    return render(request, 'manage.html')

def details(request):
    return render(request, 'details.html')

def result(request):
    return render(request, 'result.html')


def graph2d(request):
    return render(request, 'graphs/2d.html')

def graph3d(request):
    return render(request, 'graphs/3d.html')

def comparisonTable(request):
    return render(request, 'comparison.html')



