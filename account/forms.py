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
            'nid' : {'required' : 'User NID must be unique'},
        }


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
        self.fields['nid'].widget.attrs['placeholder'] = 'Your NID must be unique'

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




class UserUpdateForm(forms.ModelForm):
    nid = forms.CharField(max_length=20, required=True)
    role = forms.ChoiceField(choices=role_choices)
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email', 'nid']  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            userProfile_instance = UserProfile.objects.filter(user_account=self.instance).first()
            # for user_instance in user_instance:
            userInstance = User.objects.get(username = userProfile_instance)
            userInstance = userProfile_instance.user_account
            
            super(UserUpdateForm, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs['value'] = userInstance
            self.fields['first_name'].widget.attrs['value'] = userInstance.first_name
            self.fields['last_name'].widget.attrs['value'] = userInstance.last_name
            self.fields['email'].widget.attrs['value'] = userInstance.email
            self.fields['nid'].widget.attrs['value'] = userProfile_instance.nid
            # self.fields['role'].widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        user_instance = super().save(commit=False)
        if commit:
            user_instance.save()
            profile, created = UserProfile.objects.get_or_create(user_account=user_instance)
            print(profile)
            profile.nid = self.cleaned_data['nid']
            profile.role = self.cleaned_data['role']
            profile.save()
        return user_instance