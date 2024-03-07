from django.contrib.auth.models import User
from django.db import models

role_choices = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor')
    ]
class UserProfile(models.Model):
    user_account = models.OneToOneField(User, on_delete=models.CASCADE, related_name='accounts')
    nid = models.CharField(max_length=20, unique=True)  # Assuming NID is a string, adjust as needed
    role = models.CharField(max_length=10, choices=role_choices)
    age = models.IntegerField(null=True, blank=True)
    medical_info = models.TextField(blank=True)

    def __str__(self):
        return self.user_account.username