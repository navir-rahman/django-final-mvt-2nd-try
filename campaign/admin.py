from django.contrib import admin
from .models import Campaign, DoseBooking, CampaignReview
# Register your models here.
admin.site.register(Campaign)
admin.site.register(DoseBooking) 
admin.site.register(CampaignReview) 
