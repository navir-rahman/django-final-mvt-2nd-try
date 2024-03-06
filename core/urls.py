from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('account.urls')),
    path('campaign/', include('campaign.urls')),


]

