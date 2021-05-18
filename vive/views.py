from django.shortcuts import render
from .models import Friend
from django.views.generic import ListView

def home(request):
    context={
        'friends':Friend.objects.all(),
        'title':'Home'
    }
    return render(request,'vive/home.html',context)

def about(request):
    return render(request,'vive/about.html',{'title':'About'})

class FriendListView(ListView):
    model = Friend
    template_name = 'vive/home.html'
    context_object_name = 'friends'
    ordering = ['-date_posted']