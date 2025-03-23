from django.template.response import TemplateResponse
  
def index(request):
    return TemplateResponse(request,  "index.html")

# Create your views here.

from django.shortcuts import render
 
def index(request):
    return render(request, "index.html")
 
def about(request):
    return render(request, "about.html")
 
def contact(request):
    return render(request, "contact.html")