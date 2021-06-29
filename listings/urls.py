from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="listings"),
    path('<int:listing_id>', views.index, name="listing"),
    path('search', views.search, name="search"),
]
