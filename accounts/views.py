from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from contacts.models import Contact


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
                    messages.success(request, 'Logged in')
                    return redirect('dashboard')
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
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'You are now Logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'wrong username or password')
            return redirect('login')
    else:
        return render(request, "accounts/login.html")


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged out')
        return redirect('index')
    else:
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {'contacts': user_contacts}
    return render(request, "accounts/dashboard.html",context)
