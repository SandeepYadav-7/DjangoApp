from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def utility(request):
	return render(request, 'utility.html')

def removePunc(text):
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	new = ""
	for letter in text:
		if not(letter in punctuations):
			new += letter
	print(new)
	print("this function is working")
	return new

def output(request):
	user_text = request.GET.get("text", "Sandeep the coder")
	check = request.GET.get("punc", "off")
	# return HttpResponse(removePunc(user_text))
	if check == "on":
		output_text = removePunc(user_text)
	else:
		output_text = "You didn't choose the text formation."
	return HttpResponse(f"<h1>{output_text}</h1>")
	
	

def about(request):
	return render(request, 'about.html')