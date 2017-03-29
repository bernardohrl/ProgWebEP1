from django.shortcuts import render
from .models import User

def create_user(request):
	print(request.GET)
	context = {}
	return render(request, 'login/create_user.html', context)

