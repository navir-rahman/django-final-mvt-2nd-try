from django import forms

from .models import Vaccine, Campaign, CampaignReview, DoseBooking
from django.shortcuts import  get_object_or_404

class VaccineCampaignForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['name', 'description']
    def __init__(self, *args, **kwargs):
        super(VaccineCampaignForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your Vaccine name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter your Vaccine description'

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['campaign_name', 'campaign_description']
        
    def __init__(self, *args, **kwargs):
        super(CampaignForm, self).__init__(*args, **kwargs)
        self.fields['campaign_name'].widget.attrs['placeholder'] = 'Enter your Campaign name'  
        self.fields['campaign_description'].widget.attrs['placeholder'] = 'Enter your Campaign Description'  



class CampaignReviewForm(forms.ModelForm):
    class Meta:
        model = CampaignReview
        fields = ['rating', 'comment']
    def __init__(self, *args, **kwargs):
        super(CampaignReviewForm, self).__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs['class'] = "form-control"
        self.fields['comment'].widget.attrs['class'] = "form-control"


class DoseBookingForm(forms.ModelForm):
    
    class Meta:
        model = DoseBooking
        fields = ['first_dose_date', 'second_dose_date', 'third_dose_date', 'fourth_dose_date']
        widgets = {
            'first_dose_date': forms.DateInput(attrs={'class': 'my-2 float-none w-auto form-control', 'type': 'date'}),
            'second_dose_date': forms.DateInput(attrs={'class': 'my-2 float-none w-auto form-control', 'type': 'date'}),
            'third_dose_date': forms.DateInput(attrs={'class': 'my-2 float-none w-auto form-control', 'type': 'date'}),
            'fourth_dose_date': forms.DateInput(attrs={'class': 'my-2 float-none w-auto form-control', 'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(DoseBookingForm, self).__init__(*args, **kwargs)
        # dose = get_object_or_404(DoseBooking, pk=self.dose_id
        self.fields['first_dose_date'].widget.attrs['value'] = self.instance.first_dose_date
        self.fields['second_dose_date'].widget.attrs['value'] = self.instance.second_dose_date
        self.fields['third_dose_date'].widget.attrs['value'] = self.instance.third_dose_date
        self.fields['fourth_dose_date'].widget.attrs['value'] = self.instance.fourth_dose_date