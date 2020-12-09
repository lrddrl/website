from django.shortcuts import render

def chatroom(request):
    return render(request, 'chat/chatroom.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })