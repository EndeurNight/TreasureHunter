#lecture fichier de config

from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

config["Game"]["J1"] = {"pseudo": "Joueur 1", "score": "0"}
config["Game"]["J2"] = {"pseudo": "Joueur 2", "score": "0"}