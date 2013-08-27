from django.shortcuts import render

def footer(request):
	return render(request, 'footer.html')
