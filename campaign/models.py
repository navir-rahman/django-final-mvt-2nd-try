from django.db import models
from django.utils import timezone
from account.models import UserProfile
from vaccine.models import Vaccine

# Create your models here.
class Campaign(models.Model):
    campaign_name = models.CharField(max_length=20, blank=True, null = True)
    doctor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    vaccines = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    campaign_description = models.TextField(blank=True, max_length=100, null=True)

    # first_dose = models.DateField(null = True, blank=True )
    # second_dose = models.DateField(null = True, blank=True )
    # third_dose = models.DateField(null = True, blank=True )
    # forth_dose = models.DateField(null = True, blank=True )
    def __str__(self) -> str:
        return self.campaign_name


class DoseBooking(models.Model):
    patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    first_dose_date = models.DateField(null=True, blank=True)
    second_dose_date = models.DateField(null=True, blank=True)
    third_dose_date = models.DateField(null=True, blank=True)
    fourth_dose_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Dose Booking for {self.patient.user_account.username} in Campaign {self.campaign.campaign_name}"



class CampaignReview(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.campaign}"
