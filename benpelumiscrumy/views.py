from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from  .models import ScrumyGoals


#  def index(request):   
#       return HttpResponse("Thisss is a SSScrum AAApplication")

# def homePage(request) :
#      return HttpResponse("This is a Scrum Application")

def get_grading_parameters(request) :
      # return HttpResponse("This is a Scrum Application")
      goals = ScrumyGoals.objects.filter(goal_name = 'Learn Django')
      return HttpResponse(goals)


# def learningDjango(request) :
     

 


# get_grading_parameters"Welcome to Django"