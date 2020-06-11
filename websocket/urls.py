from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name = 'test'),
    path('connect/', views.connect, name='connect'),
    path('disconnect/', views.disconnect, name='disconnect'),
 ]