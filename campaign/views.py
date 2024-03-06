from .forms import VaccineCampaignForm, CampaignForm, CampaignReviewForm
from account.models import UserProfile
from .models import DoseBooking, Campaign, CampaignReview
from django.shortcuts import render, get_object_or_404, redirect
from datetime import timedelta
from django.utils import timezone

# Create your views here.
# def addCampaign(request):
#     form = create_campaign(request)
#     return render(request, 'makecampaign.html', {'form': form})

def addCampaign(request):
    if request.method == 'POST':
        vaccine_form = VaccineCampaignForm(request.POST)
        campaign_form = CampaignForm(request.POST)
        if vaccine_form.is_valid() and campaign_form.is_valid():
            vaccine = vaccine_form.save()
            campaign = campaign_form.save(commit=False)
            campaign.vaccines = vaccine
            print(request.user)
            userInstance = UserProfile.objects.get(user_account =request.user)
            campaign.doctor = userInstance
            campaign.save()
            return render(request, 'makecampaign.html', {'vaccine_form': vaccine_form, 'campaign_form': campaign_form})
    else:
        vaccine_form = VaccineCampaignForm()
        campaign_form = CampaignForm()
    return render(request, 'makecampaign.html', {'vaccine_form': vaccine_form, 'campaign_form': campaign_form})



def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    if request.method == 'GET':
        userInstance = UserProfile.objects.get(user_account =request.user)
        first_dose = request.GET.get('first_dose')
        print(first_dose, '\n')
        first_dose_date = timezone.datetime.strptime(first_dose, '%Y-%m-%d')
        second_dose_date = first_dose_date  + timedelta(days=3)
        third_dose_date = first_dose_date  + timedelta(days=10)
        fourth_dose_date = first_dose_date  + timedelta(days=30)
        DoseBooking.objects.get_or_create(patient=userInstance, campaign=campaign, first_dose_date=first_dose_date, second_dose_date = second_dose_date, third_dose_date=third_dose_date, fourth_dose_date=fourth_dose_date)
        # book.save()
        return render(request, 'productDetails.html', {'campaign': campaign})

    return render(request, 'productDetails.html', {'campaign': campaign})


def dose_detail(request, dose_id):
    dose = get_object_or_404(DoseBooking, pk=dose_id)
    # campaign = get_object_or_404(Campaign, pk=campaign_id)
    reviews = CampaignReview.objects.filter(campaign=dose.campaign.id)
    # if request.method == 'GET':
        # userInstance = UserProfile.objects.get(user_account =request.user)
        # first_dose = request.GET.get('first_dose')
        # print(first_dose, '\n')
        # first_dose_date = timezone.datetime.strptime(first_dose, '%Y-%m-%d')
        # second_dose_date = first_dose_date  + timedelta(days=3)
        # third_dose_date = first_dose_date  + timedelta(days=10)
        # fourth_dose_date = first_dose_date  + timedelta(days=30)
        # DoseBooking.objects.get_or_create(patient=userInstance, campaign=campaign, first_dose_date=first_dose_date, second_dose_date = second_dose_date, third_dose_date=third_dose_date, fourth_dose_date=fourth_dose_date)
        # book.save()
        # return render(request, 'dose_detail.html', {'dose': dose, 'reviews': reviews})
    campaign = get_object_or_404(Campaign, pk=dose.campaign.id)
    if request.method == 'POST':
        form = CampaignReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = UserProfile.objects.get(user_account =request.user)
            review.campaign = campaign
            review.save()
            return render(request, 'dose_detail.html', {'dose': dose, 'reviews': reviews, 'form': form})
    else:
        form = CampaignReviewForm()

    return render(request, 'dose_detail.html', {'dose': dose, 'reviews': reviews, 'form': form})




# def campaign_detail(request, campaign_id):
#     campaign = get_object_or_404(Campaign, pk=campaign_id)
#     reviews = CampaignReview.objects.filter(campaign=campaign)
#     return render(request, 'campaign_detail.html', {'campaign': campaign, 'reviews': reviews})