from django.shortcuts import render

def index(request):
    return render(request, 'chatapp/index.html')

def roomName(request, room_name):
        return render(request, 'chatapp/chatroom.html', {'room_name': room_name})