from django.shortcuts import render

def footer(request):
	return render(request, 'footer.html')

def barra_lateral(request):
	return render(request, 'barra_lateral.html')

def home(request):
	return render(request, 'home.html')