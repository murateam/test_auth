from django.shortcuts import render, redirect
from django.http import HttpResponse

# this separate function for more difficalty verification in future
def check_user(user):
	return user.is_authenticated

def check_auth(request):
	if check_user(request.user):
		return redirect('/app')
	else:
		return redirect('/accounts/login')

def app(request):
	friends = [
		{
			'name': 'Den',
			'ava': 'ava_01.png',
		},
		{
			'name': 'Charlie',
			'ava': 'ava_02.png',
		},
		{
			'name': 'Ben',
			'ava': 'ava_03.png',
		},
		{
			'name': 'Ashlie',
			'ava': 'ava_04.png',
		},

	]
	if check_user(request.user):
		# https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN
		# https://vk.com/dev/friends.get
		return render(request, 'app/app.html', {'friends': friends})
	else:
		return redirect('/accounts/login')
