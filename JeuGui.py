from ezTK import *
from random import *
from config import *
from configparser import * 
from tkinter import messagebox
import sys

global grid_cases
grid_cases = []
#grid_cases est une liste de tuples qui contient les coordonnées des cases et la distance entre la case et le trésor le plus proche (aka le score quoi)

global turns 
turns = ["J1", "J2","J2","J1","J1","J2","J2","J1","J1"]
# initiale : " + str(turns))
#turns est une liste qui contient les pseudos des joueurs pour l'ordre du jeu

global gamelevel
global win


def JeuGui(lig, col, tresors, level) :
    #lig = lignes
    #col = colonnes
    #tresors = tresors
    #level = niveau de difficulté

    global gamelevel
    gamelevel = int(level)

    print("Initialisation de la partie avec les paramètres suivants : " + str(lig) + " lignes, " + str(col) + " colonnes, " + str(tresors) + " trésors et le niveau de difficulté " + str(level))

  
  ##################
  #Création du titre de la fenêtre
    windows_title = "Treasure Hunter - Mode de jeu inconnu"

    if level == 1 : 
        windows_title = "Treasure Hunter - Facile"
    elif level == 2 :
        windows_title = "Treasure Hunter - Moyen"
    elif level == 3 :
        windows_title = "Treasure Hunter - Difficile"
    elif level == 4 :
        windows_title = "Treasure Hunter - Configuration personnalisée"

  ###############
    #Tirage au sort des trésors
    #cases est une liste de tuples (x, y) qui contient les coordonnées des trésors
    #et tant que la liste de trésors est pas pleine, on tire au sort les cordns
    cases = []

    #proteve les erreurs de config (expert mode)
    if lig*col < tresors:
        raise ValueError("There are more treasures than cases. Please check your configuration")
    
    while len(cases) < tresors :
        x = randint(0, lig-1)
        y = randint(0, col-1)
        if (x, y) not in cases :
            cases.append((x, y))

    print(str(tresors)+ " trésors ont été placés aux coordonnées suivantes : " + str(cases))
    global tresors_restants
    tresors_restants = len(cases)

    ###########################

    #La fenêtre principale du jeu
    global win

    win = Win(title=windows_title, op=1, click=on_click) #op = largeur entre les widgets

    ###############

    scoreb = Frame(win, fold=3, border=4, grow=True)
    #scorb c'est le cadre qui contiendra les scores des joueurs et le tour du joueur

    pseudo_J1 = get_pseudo('J1')
    pseudo_J2 = get_pseudo('J2')

    global J1_score 
    J1_score = Label(scoreb, text= pseudo_J1 + " = 0", border=2, grow=True, relief='flat')

    global player_turn
    player_turn = Label(scoreb, 
                        text="C'est à " + get_pseudo(turns[0]) + " de jouer",
                        border=2, grow=True)
    
    global J2_score
    J2_score = Label(scoreb, text=pseudo_J2 + " = 0", border=2, grow=True, relief='flat')

    ################
    #LA grille de jeu

    grid = Frame(win, fold=col) #fold = nombre de colonnes

    #on commence par ajouter tous les trésors dans la liste des cases
    for treso in cases:
              grid_cases.append((treso, 36))

    for i in range(lig) :
        for j in range(col) :
        #print("Coordonnées prévues par la boucle : " + str(i) + " " + str(j))
            if (i,j) in cases :
            #si la case est un trésor, on la colorie en noir + pas de texte
              colors = ('white', 'black')
              #texts = ('T', '')
              texts = ('TT', '')
            else : 
                #calcul de la distance entre la case et le trésor (distnance de Maneattan)
                distance = 100000  # disons que ça va être compliqué de faire plus que ça
                for tres in cases:
                    #print(tres)
                    d = abs(i - tres[0]) + abs(j - tres[1]) 
                    #on garde la distance mini entre la case et tous les trésors 
                    distance = min(distance, d)
                #Du coup, le texte de la case sera la distance
                texts = ('', str(distance))
              

                #coloration des cases en fonction de la distance
                if distance == 0:
                  raise ValueError("C'est pas sensé foirer ici regarde ton code au dessus")
                elif distance == 1 or distance == 2:
                  colors = ('white', 'red')
                elif distance == 3 or distance == 4 or distance == 5:
                  colors = ('white', 'yellow')
                elif distance == 6 or distance == 7 or distance == 8 or distance == 9:
                    colors = ('white', 'green')
                elif distance == 10 or distance == 11 or distance == 12 or distance == 13 or distance == 14:
                    colors = ('white', 'blue')
                else:
                    colors = ('white', 'gray')
                    
                if distance == 1 or distance == 2:
                    grid_cases.append(((i, j), 25))
                elif distance == 3 or distance == 4 or distance == 5:
                    grid_cases.append(((i, j), 16))
                elif distance == 6 or distance == 7 or distance == 8 or distance == 9:
                    grid_cases.append(((i, j), 9))
                elif distance == 10 or distance == 11 or distance == 12 or distance == 13 or distance == 14:
                    grid_cases.append(((i, j), 4))
                else:
                    grid_cases.append(((i, j), 1))

              
                #on crée la case avec les propriétés définies  
            var = Label(grid, border=2, bg=colors, text=texts, width=5, height=2)

        
          #print("State du widget : " + str(var.index))
        

    
    # colors = ("#00F", "#0F0")
    # for loop in range(lig*col):
    #     #Brick(grid, width=64, height=64, border=3, bg=colors)
    #     Label(grid, border=2, bg=colors, text=str(loop), width=5, height=2)
    #print("Voici la liste des cases (coordonnés et points): " + str(grid_cases))
    print("La liste des trésors est : " + str(cases))
    tresors_restants = len(cases)
    win.label, win.grid = win[0], win[1]
    win.loop()
    
def on_click(widget, code, mode):
  global tresors_restants
  #fonction qui gère tous les clics de souris
  #print("Widget : " + str(widget)), print("Code : " + str(code)), print("Mods : " + str(mods)), print("Master : " + str(widget.master)), print("Index : " + str(widget.index))
  if widget.master != win.grid or widget.index is None:
    return #rien a faire si on clique pas sur une case de la grille
  if code == 'LMB':
    widget.state = 1
    # print("Index de la case dnas la liste : " + str(grid_cases[i][0]))
    # print("Index du widget : " + str(widget.index))
    for val in grid_cases:
        #print("Voici l'état de la liste grid_cases : " + str(grid_cases))
        if val[0] == widget.index:
            if val[1] == 0:
                #alert eztk
                tk.messagebox.showinfo("Erreur", "La case a déjà été cliquée.")
                print("Erreur : La case a déjà été cliquée")
                return
            else :
                print("\n La case cliquée est la case : " + str(val[0]) + " et a pour score : " + str(val[1]))
                #print("La liste turns est : " + str(turns) + " et le joueur actuel est : " + str(turns[0]))
                
                if turns[0] == "J1":
                    #on ajoute le score de la case au score du joueur
                    write_config_score("J1", val[1])
                    #on récupère le score du joueur
                    points = get_score("J1")
                    update_J1_score(points)
                elif turns[0] == "J2":
                    write_config_score("J2", val[1])
                    points = get_score("J2")
                    update_J2_score(points)
                else :
                    raise ValueError("Erreur : le joueur actuel n'est pas J1 ou J2")
                #on met à zero le score de la case, pour empêcher de la recliquer
                grid_cases[grid_cases.index(val)] = (val[0], 0)
                #si la case cliquée est un trésor, on l'enlève de la liste des trésors
                if val[1] == 36:
 
                    tresors_restants -= 1
                    #si il n'y a plus de trésors, on termine la partie
                    if tresors_restants == 0:
                        global gamelevel
                        endgame(gamelevel)
                        #on quitte le jeu
                        sys.exit(0)
                # #on met à jour le tour
                update_player_turns()

    #     if grid_cases[i][0] == widget.index:

    #         write_config_score(turns[0], int(grid_cases[(widget.index)][1]))
    # #print(widget.index)

def update_J1_score(score):
    J1_score['text'] = get_pseudo("J1") + " :  " + str(score)

def update_J2_score(score):
    J2_score['text'] = get_pseudo("J2") + " :  " + str(score)

def update_player_turns():
  #on enlève le premier élément de la liste
  global turns
  turns = turns[1:]
  #si l'avant dernier et le dernier element de turns est J1, alors
  if len(turns) <= 6 and turns[-1] == "J1" and turns[-2] == "J1":
    #on ajoute un tour de J2
    turns.append("J2")
    turns.append("J2")
    turns.append("J1")
    turns.append("J1")
    #print("On ajoute un tour de J2")
  player_turn['text'] = "C'est à " + get_pseudo(turns[0]) + " de jouer"

def endgame(level) :
    #level : le niveau de difficulté (int = 1, 2, 3 ou 4)
    #on récupère les scores des joueurs

    print("Niveau : " + str(level))
    score_J1 = get_score("J1")
    score_J2 = get_score("J2")
    pseudo_J1 = get_pseudo("J1")
    pseudo_J2 = get_pseudo("J2")
    #on affiche un message de fin de partie
    if score_J1 > score_J2:
        messagebox.showinfo("Partie terminée", "Le joueur " + pseudo_J1 + " a gagné avec un score de " + str(score_J1) + " points.")
        
    elif score_J2 > score_J1:
        messagebox.showinfo("Partie terminée", "Le joueur " + pseudo_J2 + " a gagné avec un score de " + str(score_J2) + " points.")
       
    else:
        messagebox.showinfo("Partie terminée", "Egalité parfaite !" + pseudo_J1 + " et " + pseudo_J2 + " ont tous les deux " + str(score_J1) + " points.")
    
    
    
    if level not in [1, 2, 3, 4]:
        raise ValueError('Le niveau doit être 1, 2, 3 ou 4 (config expert)')
        
    
    if level == 4:
        print("Configuration personnalisée, impossible de sauvegarder les scores dans le scoreboard")
    
    if level != 4:
        write_scoreboard(pseudo_J1, score_J1, level)
        write_scoreboard(pseudo_J2, score_J2, level)

    return None

# JeuGui(2, 2, 1, 1)

