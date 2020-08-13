from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
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


def auth_success(request):
    current_user = request.user
    social_data = User.objects.get(id=current_user.id)

    vk_data = current_user.social_auth.extra().values_list()
    token = 0
    for i in vk_data:
    	for k in i:
    		if type(k) == dict:
    			token = k.get('access_token')
    # token = vk_data[0][4].get('access_token')
    response = requests.get(f'https://api.vk.com/method/friends.getOnline?v=5.52&access_token={token}')
    print(response.json())
    # {'response': [3691094, 4287067, 4298711, 5212107, 8478133, 10835985, 21165120, 24249175, 42311904, 122328958]}
    
    return HttpResponse('OK')

    # if request.user.is_authenticated:
	    # Do something for authenticated users.
	# else:
	    # Do something for anonymous users.