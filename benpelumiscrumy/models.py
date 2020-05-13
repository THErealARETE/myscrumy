from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GoalStatus(models.Model):
    status_name = models.CharField(max_length = 30)

class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length = 30)
    # goal_id 
    created_by = models.CharField(max_length = 30)
    moved_by = models.CharField(max_length = 30)
    owner = models.CharField(max_length = 30)
    goal_status = models.ForeignKey(
        GoalStatus,
        on_delete = models.PROTECT
    ) 
    user = models.ForeignKey(
        User,
        related_name = 'ScrumyGoals',
        on_delete = models.PROTECT
    )

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
