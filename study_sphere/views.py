from django.shortcuts import render
from django.urls import get_resolver
from django.http import JsonResponse

def home(request):
    return render(request, "root.html")
