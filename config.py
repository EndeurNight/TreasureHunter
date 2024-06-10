#Ce module crée des méthodes pour modifier le fichier de configuration.
#Le fichier de configuration stocke les pseudos des joueurs, leur score actualisé ainsi que la configuration de la partie.

import configparser
config = configparser.ConfigParser()

#fichier : configfiles/config.ini

def write_config_score(name, score):
    #une fonction qui prend en paramètre J1 ou J2, et qui modifie le score
    #name : str, score : int
    #name : J1 ou J2
    config.read('configfiles/config.ini')

    #si name n'est pas A ou B, on renvoie une erreur
    if name not in ['J1', 'J2']:
        raise ValueError('Le nom doit être J1 or J2, couillu regarde ton code')
    
    config.set(str(name), "score", str(score))

    with open('configfiles/config.ini', 'w') as configfile:
        config.write(configfile)

    print("Score de " + name + " mis à jour : " + str(score))

def write_config_pseudo(name, pseudo):
    #Cette fonction prend en paramètre le nom du joueur et son pseudo, et met à jour le fichier de configuration avec ces informations.
    #Elle ne prend que en paramètre que le joueur A ou B et son pseudo (sinon elle renvoie une erreur)
    #name : str, pseudo : str
    #name : que A ou B (deux joueurs pour l'instant, à voir pour plus tard)

    config.read('configfiles/config.ini')

    #si name n'est pas A ou B, on renvoie une erreur
    if name not in ['J1', 'J2']:
        raise ValueError('Le nom doit être J1 or J2, couillu regarde ton code')

    config.set(str(name), "pseudo", str(pseudo))
    with open('configfiles/config.ini', 'w') as configfile:
        config.write(configfile)
    
    print("Pseudo de " + name + " mis à jour : " + pseudo)
    
def write_config_gameconfig(type):
    #Cette fonction prend en paramètre le type de configuration (1 = facile, 2 = moyen, 3 = difficile, 4 = personnalisé) et met à jour le fichier de configuration avec ces informations.
    #Elle ne prend que en paramètre que le type de configuration (sinon elle renvoie une erreur)
    #config : int
    #config : 1, 2, 3 ou 4
    config.read('configfiles/config.ini')

    if type not in [1, 2, 3, 4]:
        raise ValueError('La configuration doit être 1, 2, 3 ou 4, ya un problème chef')
    
    #On a fixé les valeurs d'apr!s l'énonce :
    #facile : 10 lignes, 10 colonnes, 8 trésors
    #moyen : 20, 24, 10
    #difficile : 24, 36, 12

    if type == 1:
        config['gameconfig'] = {'ligne': '16', 'colonne': '12', 'tresor': '4'}
        print("Configuration facile mise à jour")
    elif type == 2:
        config['gameconfig'] = {'ligne': '20', 'colonne': '24', 'tresor': '8'}
        print("Configuration moyenne mise à jour")
    elif type == 3:
        config['gameconfig'] = {'ligne': '24', 'colonne': '36', 'tresor': '12'}
        print("Configuration difficile mise à jour")
    elif type == 4:
        print("Configuration personnalisée, on laisse la config gérer")
    
    with open('configfiles/config.ini', 'w') as configfile:
        config.write(configfile)
    
def write_scoreboard(pseudo, score, level):
    #pseudo = str, le pseudo du joueur
    #score = int, le score du J1 ou J2
    #level = int, le niveau de difficulté (1, 2 ou 3, retourne une erreur sinon)

    if level not in [1, 2, 3]:
        raise ValueError('Le niveau doit être 1, 2 ou 3, problème camarade')

    config.read(f'configfiles/score{level}.ini')

    #création d'une liste de tuples (pseudo, score) à partir du fichier de config
    scores = []
    for i in range(1, 13):
        scores.append((config[f'J{i}']['pseudo'], int(config[f'J{i}']['score'])))

    #on ajoute le score du joueur
    scores.append((pseudo, score))

    #on trie les scores
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    #on ne garde que les 12 premiers
    scores = scores[:12]

    #si le joueur a deja un score, on le remplace par son plus haut
    found = False
    for i in range(0, len(scores)):
        if scores[i][0] == pseudo:
            scores[i] = (pseudo, max(score, scores[i][1]))
            found = True
            break

    #on met à jour le fichier de config
    for i in range(0, len(scores)):
        config[f'J{i+1}']['pseudo'] = scores[i][0]
        config[f'J{i+1}']['score'] = str(scores[i][1])

    with open(f'configfiles/score{level}.ini', 'w') as configfile:
        config.write(configfile)

    if found:
        print("Scoreboard du niveau " + str(level) + " mis à jour. Nouveau score de " + pseudo + " : " + str(score))
    else:
        print("Scoreboard du niveau " + str(level) + " mis à jour. Score de " + pseudo + " mis à jour : " + str(score))

def get_scoreboard(level) :
    #En paramètre le level, retourn la liste
    if level not in [1, 2, 3, 4]:
        raise ValueError('Le niveau doit être 1, 2, 3 ou 4 (config expert), problème camarade')
    
    #si le niveau est 4, on renvoie une liste vide (je sais que c'est moche mais on est obligé de passer par ça pour Tkinter après)
    
    if level == 4 : return [[[(),()],[(),()],[(),()],[(),()],[(),()],[(),()],[(),()],[(),()],[(),()],[(),()],[(),()],[(),()]], 4]
    
    config.read(f'configfiles/score{level}.ini')

    scores = []
    for i in range(1, 13):
        scores.append((config[f'J{i}']['pseudo'], int(config[f'J{i}']['score'])))

    #on trie les scores, au cas où
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    return scores, level


# #on teste


write_scoreboard("Simon", 100, 1)
write_scoreboard("Leo", 200, 1)
write_scoreboard("Simon", 2, 2)