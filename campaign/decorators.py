from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from account.models import UserProfile

def doctor_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user_role = UserProfile.objects.get(user_account = request.user).role
        # print(user_role.role)
        if request.user.is_authenticated and user_role == 'Doctor':
            return view_func(request, *args, **kwargs)
        else:
            # Redirect or show an error page if the user doesn't have the required role
            return HttpResponseForbidden("You don't have permission to access this page. you must be a Doctor")
    return _wrapped_view

def patient_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user_role = UserProfile.objects.get(user_account = request.user).role
        if request.user.is_authenticated and user_role == 'Patient':
            return view_func(request, *args, **kwargs)
        else:
            # Redirect or show an error page if the user doesn't have the required role
            return HttpResponseForbidden("You don't have permission to access this page. you must be a patient")
    return _wrapped_view
