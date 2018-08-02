from django.db import models


def giveDefaultBoard():
    b = list()
    for i in range(64):
        b.append("0")
    b[27]="1"
    b[28]="2"
    b[35]="2"
    b[36]="1"
    return "".join(b)


class GameDB(models.Model):
    token = models.AutoField(primary_key=True)
    board = models.CharField(max_length=64, default=giveDefaultBoard())
    active_players = models.IntegerField(default=0)
    playerTurn = models.IntegerField(default=2)
    timer = models.IntegerField(default=60)
    lastValid = models.IntegerField(default=1)
    gameOver = models.IntegerField(default=0)

    def __str__(self):
        return str(self.token)
