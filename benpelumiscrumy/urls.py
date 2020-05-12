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
     path( '', views.index, name = 'index' )
]


    