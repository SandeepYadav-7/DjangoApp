from django.http import HttpResponse

def home(request):
	return HttpResponse("<h1><center>Home Section</center></h1>")

def about(request):
	return HttpResponse("<h1><center>About Section</center></h1>")

def form(request):
	return HttpResponse("<h1><center>Form Section</center></h1>")