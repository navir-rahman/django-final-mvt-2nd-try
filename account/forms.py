# account/forms.py

from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


role_choices = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor')
    ]
class UserRegistrationForm(UserCreationForm):
    nid = forms.CharField(max_length=20, required=True)
    role = forms.ChoiceField( choices=role_choices)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nid', 'role']

        # labels = {
        #     'username' : 'User Name',
        #     'password1' : "password1",
        #     'password2' : "password2",
        # }
        # widgets  = {
        #     'name' : forms.TextInput(),
        # }
        # help_texts = {
        #     'name' : "Write your full name"
        # }
        
        error_messages = {
            'username' : {'required' : 'Your name is required'},
            'password1' : {'required' : 'Use valid password'},
            'password2' : {'required' : 'User valid password'},
        }


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'

    def save(self, commit=True):
        user_account = super().save(commit=False)
        if commit == True:
            user_account.save()
            nid = self.cleaned_data.get('nid')
            role = self.cleaned_data.get('role')

            UserProfile.objects.create(
                user_account = user_account,
                nid = nid,
                role = role,
            )

        return user_account




