from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request, "objectives/index.html")

def objectives(request):
    pass

def objectives_details(request):
    pass
    
