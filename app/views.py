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
			'name': 'user1',
			'ava': 'ava_01.png',
		},
		{
			'name': 'user2',
			'ava': 'ava_02.png',
		},
		{
			'name': 'user3',
			'ava': 'ava_03.png',
		},
	]
	if check_user(request.user):
		return render(request, 'app/app.html', {'friends': friends})
	else:
		return redirect('/accounts/login')
