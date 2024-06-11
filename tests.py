#on remplit les fichiers de score avec des scores bidons

from config import *
from random import randint

for k in range (1,4) :
    for i in range(0, 12):
        prenoms = ["Léo", "Simon", "Chloé", "Celia", "Julien", "Camilia", "Léa", "Arthur", "Lucas", "Emma", "Manon", "Lola"]
        write_scoreboard(prenoms[i], randint(0, 500), k)