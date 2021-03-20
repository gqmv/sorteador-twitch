# The contents of this file are, unless where otherwise noted, licensed under https://github.com/gqmv/sorteador-twitch/LICENSE.md
import requests
import random

class user:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def increase(self):
        self.wins += 1

USERNAME = "" # Insert the streamer's username here.

request = requests.get(f"https://tmi.twitch.tv/group/user/{USERNAME}/chatters")
viewers = []
for group in request.json()["chatters"]:
    for viewer in request.json()["chatters"][group]:
        viewers.append(user(viewer))

print(f"Viewers que estão participando do sorteio:")
for viewer in viewers: print(viewer.name)

input("Para sortear, aperte enter.")
while True:
    winner = viewers[random.randint(0, len(viewers) - 1)]
    print(f"O vencedor é {winner.name}, ele já foi sorteado outras {winner.wins} vezes.")

    winner.increase()

    prompt = input("Para sortear novamente, aperte enter. Para sair, aperte N seguido de enter.").lower()

    if prompt == "n":
        break

print("Obrigado por participar :D")
print("</> por Gabriel Queiroz")
