from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def utility(request):
	return render(request, 'utility.html')