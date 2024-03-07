from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('add', views.addCampaign, name='addCampaign'),
    path('camp/<int:campaign_id>/', views.campaign_detail, name='campaign_detail'),
    path('dose/<int:dose_id>/', views.dose_detail, name='dose_detail'),
    path('all_dose/', views.all_dose, name='all_dose'),
    path('dose_detail_for_doc/<int:dose_id>/', views.dose_detail_for_doctor, name='dose_detail_for_doc'),
     path('dose_booking/<int:pk>/delete/', views.DoseBookingDeleteView.as_view(), name='dose_booking_delete'),



]
