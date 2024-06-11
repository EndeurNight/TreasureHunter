from configparser import *

config = ConfigParser()

#fichier : configfiles/config.ini

config.read('configfiles/config.ini')
config.set("GameConfig", "lignes", "20")
config.set("GameConfig", "colonnes", "24")
config.set("GameConfig", "tresors", "20")

with open('configfiles/config.ini', 'w') as configfile:
    config.write(configfile)