from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse 
from  .models import *
# import datetime
from random import randint
from django.contrib.auth.models import User

def get_grading_parameters(request) :
      goals2 = ScrumyGoals.objects.filter(goal_name = 'keep learning django')
      return HttpResponse(goals2) 



def move_goal(request, goal_id):
      
      try:
            display = ScrumyGoals.objects.get(goal_id = goal_id)
      except Exception as e:
            return render (request, 'exception.html', {'error' :'A record with that goal id does not exist'} )
      else:
            return HttpResponse(display.goal_name)
      # try:
      #       pass
      # except expression as identifier:
      #       pass
      # else:
      #       pass

def add_goal(request):
      goalId = randint(1000, 9999)
      goalStatus = GoalStatus.objects.last()
      addGoalUser = User.objects.get(username = 'louis')
      addGoal = ScrumyGoals.objects.create(goal_name = 'keep learning django', goal_id = goalId, created_by = 'Louis' , moved_by = 'Louis', owner = 'Louis' , goal_status = goalStatus ,user = addGoalUser ) 
      return addGoal

def home (request):
      # return HttpResponse("This is a Scrum Application")
      goals = ScrumyGoals.objects.filter(goal_name = 'Learn Django')
      # goals = ScrumyGoals.objects.filter(goal_id = 1)
      # return HttpResponse(goals)
      goals = "learn django"
      learnDjangoUser = User.objects.get(username = 'louis')
      scrumyValues = {'goal_name': goals , 'goal_id' : 1 ,'user' : learnDjangoUser  }
      return render(request, 'home.html' ,scrumyValues )

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


# def learningDjango(request) :
     

 


# get_grading_parameters"Welcome to Django"