from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
   
def index(request):
    return HttpResponse("<h2>Главная</h2>")
  
def about(request, name, year):
    return HttpResponse(f"""
            <h2>О машине</h2>
            <p>Марка: {name}</p>
            <p>Год: {year}</p>
    """)