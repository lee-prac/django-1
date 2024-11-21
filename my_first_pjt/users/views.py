from django.shortcuts import render
from django.http import HttpResponse


def users(request):
	return render(request, "users.html")

def profile(request, username):
	context = {
		"usersname" : username,
	}
	return render(request, "profile.html", context)