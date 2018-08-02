from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import GameDB
import threading
from time import sleep


def countdownThread(token):
    while True:
        try:
            game = GameDB.objects.get(token=token)
            game.timer = game.timer - 1
            game.save()
            sleep(1)
        except:
            print("error in thread")


def mainPage(request):
    return render(request, 'mainPage.html', {})


def newgame(request):
    # redirect here to appropriate token based url
    game = GameDB.objects.create()
    token = game.token
    return HttpResponseRedirect('/game/' + str(token))


def game(request, token):
    # get all the values of the game and pass to the function
    try:
        game = GameDB.objects.get(token=token)
        if game.active_players >= 2:
            return render(request, 'errorpage.html', {})
        game.active_players = game.active_players + 1
        game.save()
        player = 1
        if game.active_players == 2:
            player = 2
            game.timer = 60
            game.save()
            threading.Thread(target=countdownThread, args=(token,)).start()
        return render(request, 'game.html', {'game': game, 'size': range(8), 'player': player})
    except:
        # return an error page with link to homepage here
        return render(request, 'errorpage.html', {})


def refresh(request):
    token = int(request.GET['token'])
    game = GameDB.objects.get(token=token)
    data = {'board': game.board, 'playerTurn': game.playerTurn, 'timer': game.timer, 'gameOver': game.gameOver}
    return JsonResponse(data)


def update(request):
    token = int(request.GET['token'])
    board = str(request.GET['board'])
    next = int(request.GET['turn'])
    hadvalidmove = int(request.GET['hadvalidmove'])
    game = GameDB.objects.get(token=token)
    game.playerTurn = next
    game.board = board
    game.timer = 60
    if hadvalidmove == 0 and game.lastValid == 0:
        game.gameOver = 1
    elif hadvalidmove == 0:
        game.lastValid = 0
    else:
        game.lastValid = 1
    game.save()
    data = {}
    return JsonResponse(data)
