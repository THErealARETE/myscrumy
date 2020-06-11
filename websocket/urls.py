from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name = 'test'),
    path('connect/', views.connect, name='connect'),
    path('disconnect/', views.disconnect, name='disconnect'),
    path('send_message/', views.send_message, name= 'send_message'),
    path('get_recent_messages/', views.get_recent_messages, name='get_recent_messages'),
 ]