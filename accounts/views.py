from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']  # Register user
        password2 = request.POST['password2']
        if password == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
                    auth.login(request, user)
                    user.save()
                    messages.success('Logged in')
                    return redirect('index')
                else:
                    messages.error(request, 'The email is already registered')
                    return redirect('register')
            else:
                messages.error(request, 'That username is already taken.')
                return redirect('register')
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == 'POST':
        pass
    # Login user
    else:
        return render(request, "accounts/login.html")


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, "accounts/dashboard.html")
