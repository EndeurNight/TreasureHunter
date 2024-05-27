from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from expert import run_expert


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/leo/Documents/GitHub/TreasureHunter/build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    #Redirige le chemin vers le dossier assets (prévient les erreurs de chemin, Windows hihihi)
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("1004x565")
window.title("Treasure Hunter (build 1.0.8)")
window.configure(bg = "#FFFFFF")


#Création du canvas
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 565,
    width = 1004,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

###############################################################
#LES IMAGES (crées précédements avec GIMP + Figma)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    502.0,
    282.0,
    image=image_image_1
)
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    806.0,
    78.0,
    image=image_image_2
)


###############################################################
#LES BOUTONS

#Lancer la partie
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("ça va lancer le jeu, bientôt :)"),
    relief="flat"
)
button_1.place(
    x=45.0,
    y=428.0,
    width=288.0,
    height=92.0
)

#Configuration expert
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Toplevel(run_expert()),
    relief="flat"
)
button_2.place(
    x=360.0,
    y=431.0,
    width=230.0,
    height=87.0
)
###############################################################
#LES ENTRÉES (pour les pseudos)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    396.5,
    167.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=223.0,
    y=151.0,
    width=347.0,
    height=31.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    396.5,
    231.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=223.0,
    y=215.0,
    width=347.0,
    height=31.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    438.0,
    307.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=306.0,
    y=291.0,
    width=264.0,
    height=31.0
)

###############################################################

#SCOREBOARD

def scoreboard(list):
    #si la liste est vide, on renvoie rien
    if list == []:
        return None
    #si la liste dépasse 12 scores, on ne prend que les 12 premiers (par je ne sais quel miracle ahh)
    if len(list) > 12:
        list = list[:12]
    #si la liste contient au moins un pseudo, on crée son texre
    for i in range(0, len(list)):
        canvas.create_text(
            666.0,
            143.0 + (29 * i),
            anchor="nw",
            text=list[i],
            fill="#FFFFFF",
            font=("PiecesofEight", 20 * -1)
            
            )

 #pour les tests, on crée une liste de pseudos, mais prochainement, on aura une fonction qui récupère tout depuis le fichier de configuration.
list = ['test', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10', 'test11', 'test12']
scoreboard(list)

#même chose pour les scores

def score(list):
    #si la liste est vide, on renvoie rien
    if list == []:
        return None
    #si la liste dépasse 12 scores, on ne prend que les 12 premiers
    if len(list) > 12:
        list = list[:12]
    #si la liste contient au moins un score, on crée le texte correspondant
    for i in range(0, len(list)):
        canvas.create_text(
            895.0,
            143.0 + (29 * i),
            anchor="nw",
            text=list[i],
            fill="#FFFFFF",
            font=("PiecesofEight", 20 * -1)
            
            )


list = ['100', '200', '300', '400', '500', '600', '700', '800', '900', '1000', '1100', '1200']
score(list)


window.resizable(False, False)
window.mainloop()