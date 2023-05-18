from django.shortcuts import render
from .models import ChatMessage
from django.http import JsonResponse

def index(request):
    return render(request, 'chatapp/index.html')

def roomName(request, room_name):
    chat_messages = ChatMessage.objects.all()
    return render(request, 'chatapp/chatroom.html', {'room_name': room_name, 'chat_messages': chat_messages})



def save_media(request):
    if request.method == 'POST' and request.FILES.get('media'):
        media_file = request.FILES['media']
        # Save the media file to your desired location or model field
        # Example:
        # SomeModel.objects.create(media_field=media_file)
        ChatMessage.objects.create(media_field=media_file)
        media_file.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
