from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def removePunc(text):
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	new = ""
	for letter in text:
		if letter in punctuations:
			paas
		else:
			new += letter
	print(new)
	print("this function is working")
	return new

def utility(request):
	user_text = request.GET.get("text", "Sandeep the coder")
	check = request.GET.get("punc", "off")
	# return HttpResponse(removePunc(user_text))
	"""
	if check == "on":
		removePunc(user_text)
		print("working this if statement")"""
	removePunc(user_text)
	print("this file is working")
	print(f"\n{check}\n")
	return render(request, 'utility.html')

def about(request):
	return render(request, 'about.html')