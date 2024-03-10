"""
URL configuration for final_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('user/', include('django.contrib.auth.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




# user/ login/ [name='login']
# user/ logout/ [name='logout']
# user/ password_change/ [name='password_change']
# user/ password_change/done/ [name='password_change_done']
# user/ password_reset/ [name='password_reset']
# user/ password_reset/done/ [name='password_reset_done']
# user/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# user/ reset/done/ [name='password_reset_complete']
# ^(?P<path>.*)$