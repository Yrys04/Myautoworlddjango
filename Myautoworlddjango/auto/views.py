from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
 
def index(request):
    return HttpResponse("Главная страница")
 
def cars(request):
    return HttpResponse("Список машин")
 
def new(request):
    return HttpResponse("Новые автомобили")
 
def model(request):
    return HttpResponse("Наиболее популярные модели")