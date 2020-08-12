from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import *

urlpatterns = [
	# path('login/', LoginView.as_view(), name='login'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),

	path('test/', test),
]