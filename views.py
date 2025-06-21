# home/views.py
from django.shortcuts import render

def pdf(request):
    return render(request, 'pdf.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def address(request):
    return render(request, 'address.html')