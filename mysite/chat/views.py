
# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

# Create your views here.
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
