from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'), 
    path('meetings/', views.meetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('submitresource/', views.newresource, name='submitresource'),
    path('submitmeeting/', views.newmeeting, name='submitmeeting'),
]