from django.shortcuts import render
from  .models import ScrumyGoals

# Create your views here.

from django.http import HttpResponse 


def homePage(request) :
     return HttpResponse("Welcome to Django")


# def learningDjango(request) :
#      ScrumyGoals.objects.filter(goal_name = Learn Django')
#      return HttpResponse("learn django")


# def index(request):
#     return render(request, 'benpelumiscrumy/index.html', {})

# get_grading_parameters