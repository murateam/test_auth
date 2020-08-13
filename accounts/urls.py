from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout

from accounts.views import *

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]