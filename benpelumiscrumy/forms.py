#lab 19a
#Create two form classes SignupForm and CreateGoalForm. 
# The signup form will contain fields from the User model such as first_name,last_name,email,username,password
#  and the CreateGoalForm will contain the goal_name field and user field from the ScrumyGoals model. 
# The user field will enable a user of you application select the particular user the goal is being created for.

from django import forms

from .models import ScrumyGoals, User

class CreateGoalForm(forms.ModelForm):

    class Meta:
        model = ScrumyGoals
        fields = ('goal_name', 'user','goal_status')

class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','email', 'username', 'password')

class EditGoalForm(forms.ModelForm):

    class Meta:
        model = ScrumyGoals
        fields = ('goal_name', 'goal_status')