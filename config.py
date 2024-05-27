#Ce module crée des méthodes pour modifier le fichier de configuration.
#Le fichier de configuration stocke les pseudos des joueurs, leur score actualisé ainsi que la configuration de la partie.

import configparser
config = configparser.ConfigParser()

def write_score(name, score):
    #Cette fonction prend en paramètre le nom du joueur et son score, et met à jour le fichier de configuration avec ces informations.
    #Elle ne prend que en paramètre que le joueur A ou B et son score (sinon elle renvoie une erreur)
    #name : str, score : int
    #name : que A ou B (deux joueurs pour l'instant, à voir pour plus tard)

    config.read('scores.ini')

    #si name n'est pas A ou B, on renvoie une erreur
    if name not in ['A', 'B']:
        raise ValueError('Le nom doit être A or B, couillu regarde ton code')

    if name in config:
        config[name]['score'] = str(score)
    else:  
        config[name] = {'score': str(score)}
    with open('scores.ini', 'w') as configfile:
        config.write(configfile)
    
    return config

def write_pseudo(name, pseudo):
    #Cette fonction prend en paramètre le nom du joueur et son pseudo, et met à jour le fichier de configuration avec ces informations.
    #Elle ne prend que en paramètre que le joueur A ou B et son pseudo (sinon elle renvoie une erreur)
    #name : str, pseudo : str
    #name : que A ou B (deux joueurs pour l'instant, à voir pour plus tard)

    config.read('scores.ini')

    #si name n'est pas A ou B, on renvoie une erreur
    if name not in ['A', 'B']:
        raise ValueError('Le nom doit être A or B, couillu regarde ton code')

    if name in config:
        config[name]['pseudo'] = str(pseudo)
    else:  
        config[name] = {'pseudo': str(pseudo)}
    with open('scores.ini', 'w') as configfile:
        config.write(configfile)
    
    return config

def write_gameconfig(type):
    #Cette fonction prend en paramètre le type de configuration (1 = facile, 2 = moyen, 3 = difficile, 4 = personnalisé) et met à jour le fichier de configuration avec ces informations.
    #Elle ne prend que en paramètre que le type de configuration (sinon elle renvoie une erreur)
    #config : int
    #config : 1, 2, 3 ou 4
    config.read('scores.ini')

    if type not in [1, 2, 3, 4]:
        raise ValueError('La configuration doit être 1, 2, 3 ou 4, ya un problème chef')
    

    #pour facile, le nomre de ligne est 10, le nombre de colonne est 10, le nombre de trésors est 10
    #pour moyen, le nomre de ligne est 15, le nombre de colonne est 15, le nombre de trésors est 15
    #pour difficile, le nomre de ligne est 20, le nombre de colonne est 20, le nombre de trésors est 20

    if type == 1:
        config['gameconfig'] = {'ligne': '10', 'colonne': '10', 'tresor': '10'}
    elif type == 2:
        config['gameconfig'] = {'ligne': '15', 'colonne': '15', 'tresor': '15'}
    elif type == 3:
        config['gameconfig'] = {'ligne': '20', 'colonne': '20', 'tresor': '20'}
    elif type == 4:
        print("Configuration personnalisée, on laisse l'expert gérer")
    with open('scores.ini', 'w') as configfile:
        config.write(configfile)

#on teste

write_score('A', 100)
write_score('A', 200)
write_score('B', 300)
write_pseudo('A', 'test')
write_pseudo('B', 'test2')
write_gameconfig(1)
write_gameconfig(2)
write_gameconfig(3)






