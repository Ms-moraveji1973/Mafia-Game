from django.shortcuts import render
from .models import MafiaRoleModel
from random import shuffle
# Create your views here.

def mafia(request):
    if request.method == 'POST':
        num_players = int(request.POST['mafia_player'])
        mafia_players = int(num_players / 3)
        ken_player = 1
        leon_player = 1
        doctor_player = 1
        constantine_player = 1
        nostradamus_player = 1
        if num_players-mafia_players-ken_player-leon_player-doctor_player-constantine_player-nostradamus_player != 0 :
            citizen_player = int(num_players-mafia_players-ken_player-leon_player-doctor_player-constantine_player-nostradamus_player)
        else:
            citizen_player = 0
        players = []
        for i in range(num_players):
            players.append(MafiaRoleModel())

        print(players)

        mafia_role = ['mafia'] * mafia_players
        shuffle(mafia_role)
        ken_role = ['ken'] * 1
        leon_player = ['leon_player'] * 1
        doctor_player = ['doctor_player'] * 1
        constantine_player = ['constantine_player'] * 1
        ken_role = ['ken'] * 1
        nostradamus_player = ['nostradamus_player'] * 1
        citizen_role = ['citizen'] * citizen_player 
        all_role = mafia_role + citizen_role + leon_player + doctor_player + constantine_player + nostradamus_player + ken_role   
        shuffle(all_role)
        for i in range(num_players):
            players[i].name = f"Player {i+1}"
            players[i].role = all_role[i]

        return render(request , 'game.html' , {'players':players    })
    else:
        return render(request ,'home.html')

