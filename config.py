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
    
    return config

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
    elif type == 2:
        config['gameconfig'] = {'ligne': '20', 'colonne': '24', 'tresor': '8'}
    elif type == 3:
        config['gameconfig'] = {'ligne': '24', 'colonne': '36', 'tresor': '12'}
    elif type == 4:
        print("Configuration personnalisée, on laisse la config gérer")
    
    with open('configfiles/config.ini', 'w') as configfile:
        config.write(configfile)


with open('configfiles/config.ini', 'w') as configfile:
        config.write(configfile)



#on teste


write_config_score('J1', 10)
write_config_score('J1', 15)

write_config_score('J2', 10)
write_config_score('J2', 13)





