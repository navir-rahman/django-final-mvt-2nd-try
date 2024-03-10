from .forms import VaccineCampaignForm, CampaignForm, CampaignReviewForm, DoseBookingForm
from account.models import UserProfile
from .models import DoseBooking, Campaign, CampaignReview
from django.shortcuts import render, get_object_or_404, redirect
from datetime import timedelta
from django.utils import timezone
from .decorators import doctor_required, patient_required
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect


# Create your views here.
# def addCampaign(request):
#     form = create_campaign(request)
#     return render(request, 'makecampaign.html', {'form': form})
@doctor_required
def addCampaign(request):
    user_role_doctor =False
    if request.user.is_authenticated:
        var = UserProfile.objects.filter(user_account=request.user).first()
        if var.role == 'Doctor':
            user_role_doctor = True

    if request.method == 'POST':
        vaccine_form = VaccineCampaignForm(request.POST)
        campaign_form = CampaignForm(request.POST)
        if vaccine_form.is_valid() and campaign_form.is_valid():
            vaccine = vaccine_form.save()
            campaign = campaign_form.save(commit=False)
            campaign.vaccines = vaccine

            userInstance = UserProfile.objects.get(user_account =request.user)
            campaign.doctor = userInstance
            campaign.save()



            return render(request, 'makecampaign.html', {'vaccine_form': vaccine_form, 'campaign_form': campaign_form, 'user_role_doctor': user_role_doctor})
    else:


        vaccine_form = VaccineCampaignForm()
        campaign_form = CampaignForm()
    return render(request, 'makecampaign.html', {'vaccine_form': vaccine_form, 'campaign_form': campaign_form, 'user_role_doctor': user_role_doctor})



def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    user_role_doctor =False
    if request.user.is_authenticated:
        var = UserProfile.objects.filter(user_account=request.user).first()
        if var.role == 'Doctor':
            user_role_doctor = True

    if request.method == 'GET':
        userInstance = UserProfile.objects.get(user_account =request.user)
        first_dose = request.GET.get('first_dose')
        if first_dose != None:
            print(first_dose, '\n')
            first_dose_date = timezone.datetime.strptime(first_dose, '%Y-%m-%d')
            second_dose_date = first_dose_date  + timedelta(days=3)
            third_dose_date = first_dose_date  + timedelta(days=10)
            fourth_dose_date = first_dose_date  + timedelta(days=30)
            DoseBooking.objects.get_or_create(patient=userInstance, campaign=campaign, first_dose_date=first_dose_date, second_dose_date = second_dose_date, third_dose_date=third_dose_date, fourth_dose_date=fourth_dose_date)
        # book.save()
        return render(request, 'productDetails.html', {'campaign': campaign, 'user_role_doctor': user_role_doctor})

    return render(request, 'productDetails.html', {'campaign': campaign, 'user_role_doctor': user_role_doctor})


def dose_detail(request, dose_id):
    user_role_doctor =False
    if request.user.is_authenticated:
        var = UserProfile.objects.filter(user_account=request.user).first()
        if var.role == 'Doctor':
            user_role_doctor = True

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
            return render(request, 'dose_detail.html', {'dose': dose, 'reviews': reviews, 'form': form, 'user_role_doctor': user_role_doctor})
    else:
        form = CampaignReviewForm()

    return render(request, 'dose_detail.html', {'dose': dose, 'reviews': reviews, 'form': form, 'user_role_doctor': user_role_doctor})




# def campaign_detail(request, campaign_id):
#     campaign = get_object_or_404(Campaign, pk=campaign_id)
#     reviews = CampaignReview.objects.filter(campaign=campaign)
#     return render(request, 'campaign_detail.html', {'campaign': campaign, 'reviews': reviews})




def all_dose(request):
    user_role_doctor =False
    if request.user.is_authenticated:
        var = UserProfile.objects.filter(user_account=request.user).first()
        if var.role == 'Doctor':
            user_role_doctor = True

    all_dose = DoseBooking.objects.all()
    return render(request, 'shop.html', {'all_dose': all_dose, 'user_role_doctor': user_role_doctor})




def dose_detail_for_doctor(request, dose_id):
    user_role_doctor =False
    if request.user.is_authenticated:
        var = UserProfile.objects.filter(user_account=request.user).first()
        if var.role == 'Doctor':
            user_role_doctor = True

    dose = get_object_or_404(DoseBooking, pk=dose_id)
    reviews = CampaignReview.objects.filter(campaign=dose.campaign.id)
    dose_form = DoseBookingForm(instance = dose)
    form = CampaignReviewForm()
    if request.method == 'GET':
        dose_form = DoseBookingForm(request.POST, instance=dose)
        if dose_form.is_valid():
            if request.GET.get('first_dose_date') is not None:
                dose.first_dose_date = request.GET.get('first_dose_date')
                dose.second_dose_date = request.GET.get('second_dose_date')
                dose.third_dose_date = request.GET.get('third_dose_date')
                dose.fourth_dose_date = request.GET.get('fourth_dose_date')
                dose.save()
                return redirect('dose_detail_for_doc', dose_id=dose_id)
    return render(request, 'dose_detail.html', {'dose': dose, 'reviews': reviews, 'form': form, 'page': 'dose_detail_for_doctor', 'dose_form': dose_form, 'user_role_doctor': user_role_doctor})



class DoseBookingDeleteView(DeleteView):
    model = DoseBooking
    success_url = reverse_lazy('all_dose')  # Replace 'success_url_name' with the name of the URL to redirect after deletion
    template_name = None  # Set template_name to None to bypass template lookup

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)