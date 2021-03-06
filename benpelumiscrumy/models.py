from django.db import models
from django.contrib.auth.models import User
from random import randint

# Create your models here.

class GoalStatus(models.Model):
    status_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.status_name    
# default = 1,unique=True,
class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length = 30)
    goal_id = models.IntegerField(default = 4,  unique = True )
    created_by = models.CharField(max_length = 30)
    moved_by = models.CharField(max_length = 30)
    owner = models.CharField(max_length = 30)
    # goal_description = models.TextField()
    goal_status = models.ForeignKey(
        GoalStatus,
        on_delete = models.PROTECT,
        related_name='scrumy_goal',
        # null = True
    ) 
    user = models.ForeignKey(
        User,
        on_delete = models.PROTECT,
        related_name = 'goal_owner'
    )

    def __str__(self):
        return self.goal_name
       

class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length = 30)
    created_by = models.CharField(max_length = 30)
    moved_from = models.CharField(max_length = 50)
    moved_to = models.CharField(max_length = 50)
    time_of_action = models.DateField()
    goal = models.ForeignKey(
        ScrumyGoals,
        on_delete = models.PROTECT
    )
    def __str__(self):
        return self.created_by 