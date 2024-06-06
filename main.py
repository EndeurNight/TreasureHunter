#importation des modules
from configparser import *
from os import path

def create_score_file():
    for i in range(1,4) : 
        print(f"Checking for score file {i}...")
        if not path.exists(f'configfiles/score{i}.ini'):
            print("Creating score file...")
            with open(f'configfiles/score{i}.ini', 'w') as configfile:
                config = ConfigParser()
                config.add_section("GameConfig")
                config.set("GameConfig", "mode", f"{i}")
                for j in range(1, 13) :
                    config.add_section(f"J{j}")
                    config.set(f"J{j}", "pseudo", "")
                    config.set(f"J{j}", "score", "0")
                config.write(configfile)
                print(f"Score file {i} created")
        else : 
            print("Config file already exists. Pray that it's not corrupted")




def launch() : 
    print(r"""
    
 _____                                                      _            
/__   \_ __ ___  __ _ ___ _   _ _ __ ___  /\  /\_   _ _ __ | |_ ___ _ __ 
  / /\/ '__/ _ \/ _` / __| | | | '__/ _ \/ /_/ / | | | '_ \| __/ _ \ '__|
 / /  | | |  __/ (_| \__ \ |_| | | |  __/ __  /| |_| | | | | ||  __/ |   
 \/   |_|  \___|\__,_|___/\__,_|_|  \___\/ /_/  \__,_|_| |_|\__\___|_|   
                                                                         
                Made with love by Simon and Leo <3
                                                          
    """)
    print("TreasureHunter V1.6.2" + "\n")
    print("Initializing...")
    config = ConfigParser()

    # parse existing file
    config.read('configfiles/config.ini')

    print("Checking for config file...")

    #Section de configuration du jeu
    if not path.exists('configfiles/config.ini'):
        print("Creating config file...")
        config.add_section("GameConfig")
        config.set("GameConfig", "lignes", "10")
        config.set("GameConfig", "colonnes", "10")
        config.set("GameConfig", "tresors", "10")
        #Section des joueurs
        config.add_section("J1")
        config.set("J1", "pseudo", "")
        config.set("J1", "score", "0")
        config.add_section("J2")
        config.set("J2", "pseudo", "")
        config.set("J2", "score", "0")
        with open('configfiles/config.ini', 'w') as configfile:
            config.write(configfile)
        print("Config file created")
    else:
        print("Config file already exists. Pray that it's not corrupted")
    #vérification des scores
    create_score_file()
    print("Starting GUI...")
    #on lance la fenêtre de démarrage
    from MenuGui import MenuGui
    MenuGui()
    print("GUI started")
    

if __name__ == "__main__" :
    launch()
