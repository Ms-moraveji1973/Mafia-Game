from django.shortcuts import render
from random import shuffle
from .models import MafiaRoleModel , CartModel
from .forms import NumberForm
# Create your views here.

def mafia(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid() :
            num_players = form.cleaned_data['mafia_player']
            godfather_player = 1
            goodman_player = 1
            matador_player = 1
            grup_mafia = goodman_player + matador_player + godfather_player
            if num_players > 11 :
                mafia_players = int((num_players / 3) - grup_mafia)
                print(mafia_players)
            else :
                mafia_players = 0
            ken_player = 1
            leon_player = 1 
            doctor_player = 1
            constantine_player = 1
            nostradamus_player = 1
            Citizenshipـroles = ken_player + leon_player + doctor_player + constantine_player +  nostradamus_player
            Mafias_roles = godfather_player + matador_player + matador_player + mafia_players
            if num_players - Citizenshipـroles - Mafias_roles  != 0 :
                citizen_player = int(num_players -Citizenshipـroles - Mafias_roles )
                print(citizen_player)
            else:
                citizen_player = 0
            players = []
            for i in range(num_players):
                players.append(MafiaRoleModel())
            mafia_role = ['Mafia'] * mafia_players
            shuffle(mafia_role)
            godfather_role = ['GodFather'] * godfather_player
            goodman_role = ['GoodMan'] * goodman_player
            matador_role = ['Matador'] * matador_player
            ken_role = ['Ken'] * ken_player
            leon_role = ['Leon'] * leon_player
            doctor_role = ['Doctor'] * doctor_player
            constantine_role = ['Constantine'] * constantine_player
            nostradamus_role = ['Nostradamus'] * 1
            citizen_role = ['Citizen'] * citizen_player 
            all_role = mafia_role + citizen_role + leon_role + doctor_role + constantine_role + nostradamus_role + ken_role + godfather_role + goodman_role + matador_role  
            shuffle(all_role)
            for i in range(num_players):
                players[i].name = f"Player {i+1}"
                players[i].role = all_role[i]
        
            return render(request , 'game.html' , {'players':players})
        else :
            return render(request , 'home.html' , {'form':form})
    else:
        form = NumberForm()
        return render(request ,'home.html' , {'form':form})


def cart(request):
    carts = []

    for i in range(0,5):
        carts.append(CartModel())
    silence = ['سکوت برره ها'] * 1
    face_off = ['تغییر چهره'] * 1
    imagin = ['ذهن زیبا'] * 1
    person = ['افشای هویت'] * 1
    dastband = ['دستبند '] * 1
    all_carts = silence + face_off + imagin + person+  dastband
    shuffle(all_carts)
    for i in range (0,len(carts)) :
        carts[i].cart_id = f"Number{i+1}"
        carts[i].cart = all_carts[i]

    for cart in carts :
        cart.save()
    return render(request , 'cart.html' , {'carts' : carts})

