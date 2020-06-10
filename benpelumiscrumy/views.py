from django.shortcuts import render, redirect
from django.http import HttpResponse 
from  .models import *
from .forms import *
# import datetime
from random import randint
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.urls import reverse


#lab 19b
# Reconstruct your index view such that it is used to create a new user account on your application.
#  When a GET request is sent to the view the view should render an empty SignupForm on an index.html template
#  and if its a POST request, all the form data should be processed and saved on the database.
def index(request) :
      if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                 temp =  form.save(commit = False)   
                 temp.set_password(request.POST.get('password'))
                 temp.save()                          
                 my_group = Group.objects.get(name='Developer') 
                 users = User.objects.get(username = temp.username) 
                 my_group.user_set.add(users)
                 return redirect('/benpelumiscrumy/accounts/login/')
            else:
                  print (form.errors)
      else:
            form = SignUpForm()
      SigUpForm = {'form': form}
      return render( request , 'benpelumiscrumy/signUp.html', SigUpForm)
      # goals = 'keep learning django'
      # return HttpResponse(goals) 
   
 
@login_required(login_url='../accounts/login') 
def move_goal(request , goal_id):
      dictionary = {'error': 'A record with that goal id does not exist'}
      validUser = request.user
      try: 
        obj = ScrumyGoals.objects.get(goal_id = goal_id)
      except ObjectDoesNotExist:
         return render(request, 'benpelumiscrumy/exception.html', dictionary) 
      else:   
         if validUser.is_authenticated:
            if validUser.groups.filter(name = 'Developer').exists():
               if request.method == 'POST':
                  form = EditGoalForm(request.POST, instance= obj)
                  if obj.user == validUser:
                     if form.is_valid():
                        if GoalStatus.objects.get(status_name = 'Done Goal') != obj.goal_status:
                           new_goal = form.save(commit = False)
                           new_goal.save()
                           return redirect('/benpelumiscrumy/home/')

                        else:
                           return HttpResponse('your not permitted to move to done goal')   
                        
                  else:
                     return HttpResponse('you can only move your goals')   
      
               else:
                  form = EditGoalForm(instance=obj)
               return render(request, 'benpelumiscrumy/addGoal.html', {'form': form})   
            elif validUser.groups.filter(name = 'Quality Assurance').exists():
               if request.method == 'POST':
                  form = EditGoalForm(request.POST, instance=obj)   
                  if form.is_valid():
                     new_goal = form.save(commit = False)
                     new_goal.save()
                     return redirect('/benpelumiscrumy/home/')
                
               else:
                  form = EditGoalForm(instance=obj)
               return render(request, 'benpelumiscrumy/addGoal.html', {'form': form})

            elif validUser.groups.filter(name = 'Admin').exists(): 
               if request.method == 'POST':
                  form =  EditGoalForm(request.POST, instance=obj)  
                  if form.is_valid():
                     new_goal = form.save(commit = False)
                     new_goal.save()
                     return redirect('/benpelumiscrumy/home/')

               else:
                  form = EditGoalForm(request.POST, instance = obj)
               return render(request, 'benpelumiscrumy/addGoal.html', {'form': form})    

            elif validUser.groups.filter(name = 'Owner').exists(): 
               if request.method == 'POST':
                  form = EditGoalForm(request.POST, instance=obj )
                  if obj.user == validUser:
                     if form.is_valid():
                        new_goal = form.save(commit = False)
                        new_goal.save()
                        return redirect('/benpelumiscrumy/home')     
                  else:
                     return HttpResponse('not this users goal')
               else:
                  form = EditGoalForm(request.POST, instance = obj)
               return render(request, 'benpelumiscrumy/addGoal.html', {'form': form}) 
            else:
               form = EditGoalForm(request.POST, instance = obj)
            return render(request, 'benpelumiscrumy/addGoal.html', {'form': form}) 



@login_required(login_url='../accounts/login')
def add_goal(request):  
      validUser = request.user
      if validUser.is_authenticated:
         if validUser.groups.filter(name= 'Developer').exists() or validUser.groups.filter(name = 'Quality Assurance').exists() or validUser.groups.filter(name= 'Owner').exists():
            temp = CreateGoalForm()
            if request.method == 'POST':   
               temp = CreateGoalForm(request.POST)
               if temp.is_valid():
                  temp = temp.save(commit = False)
                  # temp.goal_status = GoalStatus.objects.create(status_name = 'Done Goal')
                  temp.goal_status = GoalStatus.objects.last()
                  temp.user = validUser
                  temp.goal_id = randint(1000, 9999) 
                  temp.save()
                  return redirect('/benpelumiscrumy/home/')
               else:
                  print (temp.errors)
            else:
               form = CreateGoalForm()
            GoalFormDictionary = {'form': form, 'user': validUser}
            return render( request , 'benpelumiscrumy/addGoal.html', GoalFormDictionary)
         else:
            return HttpResponse('you are not allowed to create a goal')      
      else:
         return HttpResponse('please sign in')

     
     
# LAB 16
#  1
    #    With your home view in place, redefine it such that it passes a context containing 
    #    the following dictionary values to the home.html template for rendering: 
    #    I) all existing users on the User model. 
    #    II) every goal that falls under Weekly Goals 
    #    II) All goals under Daily Goals 
    #    IV) All goals under Verify Goals
    #     V) All goals under Done Goals

#  2    
    # While maintaining the current table headings of your html table,
    # construct the table body such that a particular user instance occupies
    # one row of the table with the username occupying the user column 
    # and all its goals should also fall within that row.
    # Ensure that any goal with a status Weekly Goal will fall under the column weekly goal,
    # any goal with status Daily Goal will fall under the column Daily Goals same should apply to verify
    #  and Done goals with each goal having its goal_id and goal_name being displayed.


@login_required(login_url='../accounts/login')
def home (request):
      user = User.objects.all()
      # obj = ScrumyGoals.objects.get(goal_id = goal_id)
      # obj2 = obj.goal_id
      # obj = args = (obj2))

      allWeeklyGoals = GoalStatus.objects.get(status_name = 'Weekly Goal')
      allWeeklyGoals = allWeeklyGoals.scrumy_goal.all()

      allDailyGoals = GoalStatus.objects.get(status_name = 'Daily Goal')
      allDailyGoals = allDailyGoals.scrumy_goal.all()

      allVerifyGoals = GoalStatus.objects.get(status_name = 'Verify Goal')
      allVerifyGoals = allVerifyGoals.scrumy_goal.all()

      allDoneGoals = GoalStatus.objects.get(status_name = 'Done Goal')
      allDoneGoals = allDoneGoals.scrumy_goal.all()

      dictionaryValues = { 'users': user , 'weekly_goals': allWeeklyGoals, 'daily_goals': allDailyGoals,
                         'verify_goals': allVerifyGoals , 'done_goals': allDoneGoals, }
      return render(request, 'benpelumiscrumy/home.html' ,dictionaryValues )


# def get_absolute_url (self):
#       return reverse('movegoal', kwargs = {'id', self.id})

def homealone (request, goal_id):
      obj = ScrumyGoals.objects.get(goal_id = goal_id)
      user = User.objects.get()
      return HttpResponse(obj.goal_id)
# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


# def learningDjango(request) :
     
# goalId = randint(1000, 9999)
      # goalStatus = GoalStatus.objects.last()
      # addGoalUser = User.objects.get(username = 'louis')
      # addGoal = ScrumyGoals.objects.create(goal_name = 'keep learning django', goal_id = goalId, created_by = 'Louis' , moved_by = 'Louis', owner = 'Louis' , goal_status = goalStatus ,user = addGoalUser ) 
      # return HttpResponse(addGoal)
 


# get_grading_parameters"Welcome to Django"