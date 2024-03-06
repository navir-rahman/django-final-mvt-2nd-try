from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserRegistrationForm, UserUpdateForm
from .models import UserProfile
from django.views import View

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')  
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('register')


# def profile(request):
#     if request.method == 'POST':
#         form = UserUpdateForm(instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = UserUpdateForm(instance=request.user)
#     return render(request, 'accounts/profile.html', {'form': form})

class profile(View):
    template_name = 'accounts/profile.html'
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name , {'form': form})
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})