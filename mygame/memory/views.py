from django.shortcuts import render

# Create your views here.
def game_home(request):
    return render(request,'memory/game.html')