from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 


def homePage(request) :
     return HttpResponse("Welcome to Django")

# def index(request):
#     return render(request, 'benpelumiscrumy/index.html', {})

# get_grading_parameters