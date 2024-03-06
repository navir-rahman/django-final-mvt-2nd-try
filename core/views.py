from django.shortcuts import render
# Create your views here.
from campaign.models import Campaign, DoseBooking
def home(request):
    all_campaigns = Campaign.objects.all()
    all_dose = DoseBooking.objects.all()

    return render(request, 'home.html', {'campaigns':all_campaigns, 'all_dose':all_dose})