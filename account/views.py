from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserRegistrationForm, UserUpdateForm
from .models import UserProfile
from django.views import View

# email
from django.core.mail import EmailMultiAlternatives


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # send email notification
            # token = default_token_generator.make_token(user)
            # print("token ", token)
            # uid = urlsafe_base64_encode(force_bytes(user.pk))
            # print("uid ", uid)
            # confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            # email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            email_body = f'your id is created'
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            es = email.send()
            print(es)


            return redirect('register')  
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')


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