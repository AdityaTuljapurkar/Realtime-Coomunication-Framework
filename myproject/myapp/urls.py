from django.contrib import admin
from django.urls import path , include
from myapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('room',views.room,name='room'),
    path('checkhome',views.checkhome,name='checkhome'),
    path('createRoom',views.createRoom,name='createRoom'),
    path('CreateNewRoom',views.CreateNewRoom,name='CreateNewRoom'),
]