from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import requests

from accounts.forms import LoginForm

class LoginView(View):
	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(
				request,
				username=cd['username'],
				password=cd['password']
			)
			if user is None:
				return HttpResponse('Неправильный логин и/или пароль')

			if not user.is_active:
				return HttpResponse('Ваш аккаунте заблокирован')

			login(request, user)
			# return HttpResponse('Добро пожаловать! Успешный вход')
			return render(request, 'accounts/login.html', {'form':form})

		return render(request, 'accounts/login.html', {'form':form})

	def get(self, request, *args, **kwargs):
		form = LoginForm
		return render(request, 'accounts/login.html', {'form': form})

def test(request):
	#login.vk.com/?act=openapi&oauth=1&aid=745344&location=127.0.0.1&new=1&response_type=code
	r = requests.get('login.vk.com/?act=openapi&oauth=1&aid=7563437&location=127.0.0.1&new=1&response_type=code')
	print(r)
	return HttpResponse('call test')

def sample_view(request):
    current_user = request.user
    print current_user.id

    if request.user.is_authenticated:
	    # Do something for authenticated users.
	else:
	    # Do something for anonymous users.