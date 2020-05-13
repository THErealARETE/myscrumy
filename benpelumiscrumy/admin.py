from django.contrib import admin

# Register your models here.

from .models import ScrumyGoals, GoalStatus,ScrumyHistory

admin.site.register(ScrumyHistory)
admin.site.register(GoalStatus)
admin.site.register(ScrumyGoals)