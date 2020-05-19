from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse 
from  .models import ScrumyGoals
import datetime


#  def index(request):   
#       return HttpResponse("Thisss is a Scrum Application")

# def homePage(request) :
#      return HttpResponse("This is a Scrum Application")

def get_grading_parameters(request) :
      return HttpResponse("This is a Scrum Application")
      # goals = ScrumyGoals.objects.filter(goal_name = 'Learn Django')
      # return HttpResponse(goals)

# def move_goal(request) :
# receive a request object and a goal_id from the url
# use received value to query database for a goal with the goal_id 
#  return the goal in the httpresponse , use get instead of fiter for the response

def move_goal(request, goal_id):
      display = ScrumyGoals.objects.get(goal_id = goal_id)
      return HttpResponse(display)




# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


# def learningDjango(request) :
     

 


# get_grading_parameters"Welcome to Django"