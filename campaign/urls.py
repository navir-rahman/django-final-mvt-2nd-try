from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('add', views.addCampaign, name='addCampaign'),
    path('camp/<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
    path('dose/<int:dose_id>/', views.dose_detail, name='dose_detail'),



]
