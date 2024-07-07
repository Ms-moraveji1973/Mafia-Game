from django.shortcuts import render
from .models import MafiaRoleModel
from random import shuffle
# Create your views here.

def mafia(request):
    if request.method == 'POST':
        num_players = int(request.POST['mafia_player'])
        mafia_players = int(num_players / 3)
        citizen_player = int(num_players-mafia_players)

        players = []
        for i in range(num_players):
            players.append(MafiaRoleModel())

        mafia_role = ['mafia'] * mafia_players
        shuffle(mafia_role)
        citizen_role = ['citizen'] * citizen_player 
        all_role = mafia_role + citizen_role
        shuffle(all_role)
        for i in range(num_players):
            players[i].name = f"Player {i+1}"
            players[i].role = all_role[i]

        return render(request , 'game.html' , {'players':players    })
    else:
        return render(request ,'home.html')

