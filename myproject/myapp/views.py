from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def room(request):
    return render(request,'room.html')



def checkhome(request):
    username = request.POST['username']
    room = request.POST['room']
    if Home.objects.filter(room =room).exists():
        return redirect('/'+room+'/?username='+username)
    else : 
        error = str("The room : "+ room+" does not exist")

        return  render(request,"home.html",{
            'error':error,
        })

def createRoom(request):
    return render (request,'createRoom.html')

def CreateNewRoom(request):
    username = request.POST.get('username')
    room = request.POST.get('room')
    if Home.objects.filter(room =room).exists():
        output = "The room already exist"
    else :
        new_room =Home.objects.create(room = room , name = username)
        new_room.save()
        output = "The room has been created"
    return render(request,"home.html",{
        'output':output,
    })