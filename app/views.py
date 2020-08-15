from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

# this separate function for more complexy verification in future
def check_user(user):
	return user.is_authenticated

def check_auth(request):
	if check_user(request.user):
		return redirect('/app')
	else:
		return redirect('/accounts/login')

def app(request):
	if check_user(request.user):

		vk_data = request.user.social_auth.extra().values_list()
		user_id = 0
		user_token = 0
		for i in vk_data:
			for k in i:
				if type(k) == dict:
					user_id = k.get('id')
					user_token = k.get('access_token')

		version = 5.52
		count = 5
		order = 'random'

		# response = requests.get(f'https://api.vk.com/method/friends.get?v=5.52&uid={user_id}&access_token={user_token}&count=5')
		response = requests.get(
			'https://api.vk.com/method/friends.get',
			{
				'v': version,
				'user_id': user_id,
				'access_token': user_token,
				'count': count,
				'order': order,
				'fields': 'id,photo_100'
			},
		)
		friends = response.json()['response']['items']


		return render(request, 'app/app.html', {'friends': friends})
	else:
		return redirect('/accounts/login')
