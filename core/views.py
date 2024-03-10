from django.shortcuts import render
from account.models import UserProfile
# Create your views here.
from campaign.models import Campaign, DoseBooking
def home(request):
    all_campaigns = Campaign.objects.all()
    all_dose = DoseBooking.objects.all()

    user_role_doctor =False
    if request.user.is_authenticated:
        var = UserProfile.objects.filter(user_account=request.user).first()
        if var.role == 'Doctor':
            user_role_doctor = True

    return render(request, 'home.html', {'campaigns':all_campaigns, 'all_dose':all_dose, 'user_role_doctor': user_role_doctor})