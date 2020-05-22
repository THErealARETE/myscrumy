# from django.urls import path
# from benpelumiscrumy import views


# urlpatterns = [
#     path('', views.homePage, name='home'),
# ]

from django.urls import path
# from .views import homePage
from benpelumiscrumy import views


urlpatterns = [
    # path('', homePage, name='home'),
     path( '', views.get_grading_parameters, name = 'index' ),
    #  path('movegoal/<int:goal_id>', views.move_goal),
     path('addgoal/',views.add_goal),
     path('home/',views.home),
    #  path('exception/', views.move_goal)
]


    