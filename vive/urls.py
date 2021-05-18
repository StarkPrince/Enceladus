from django.urls import path
from . import views
from .views import FriendListView

urlpatterns = [
    path('', FriendListView.as_view(), name="vive-home"),
    path('about/', views.about, name="vive-about"),
]