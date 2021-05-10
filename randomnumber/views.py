from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from random import randint
from django.contrib import messages
# Create your views here.

    
def display(request):
 
    return render(request,"home.html")