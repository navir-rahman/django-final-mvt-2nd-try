from django import forms

from .models import Vaccine, Campaign, CampaignReview

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
        fields = ['campaign_name', 'start_date']
        
    def __init__(self, *args, **kwargs):
        super(CampaignForm, self).__init__(*args, **kwargs)
        self.fields['campaign_name'].widget.attrs['placeholder'] = 'Enter your Campaign name'




class CampaignReviewForm(forms.ModelForm):
    class Meta:
        model = CampaignReview
        fields = ['rating', 'comment']
    def __init__(self, *args, **kwargs):
        super(CampaignReviewForm, self).__init__(*args, **kwargs)
        self.fields['rating'].widget.attrs['class'] = "form-control"
        self.fields['comment'].widget.attrs['class'] = "form-control"