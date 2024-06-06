from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from ExpertGui import run_expert


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/leo/Documents/GitHub/TreasureHunter/assets/frame0")

def relative_to_assets(path: str) -> Path:
    #Redirige le chemin vers le dossier assets (prévient les erreurs de chemin, Windows hihihi)
    return ASSETS_PATH / Path(path)


def menugui(list):
    #list : la liste des pseudos et scores des joueurs.
    #Exemple : list = ['[pseudo1, score1]', '[pseudo2, score2]', '[pseudo3, score3]',...]

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
                text=list[i][0],
                fill="#FFFFFF",
                font=("PiecesofEight", 20 * -1)
                
                )

        #même chose pour les scores

        #si la liste est vide, on renvoie rien
        if list == []:
            return None
        #si la liste dépasse 12 scores, on ne prend que les 12 premiers (au cas où, on ne sait jamais lol)
        if len(list) > 12:
            list = list[:12]
        #si la liste contient au moins un score, on crée le texte correspondant
        for i in range(0, len(list)):
            canvas.create_text(
                895.0,
                143.0 + (29 * i),
                anchor="nw",
                text=list[i][1],
                fill="#FFFFFF",
                font=("PiecesofEight", 20 * -1)
                
                )

        window.resizable(False, False)
        window.mainloop()

test_list = [['JDHNKAZJNDJKZAO', '100'], ['Lédzadzadzao', '200'], ['PierrdzadzazadzadzabdfjkbzefrkjbezkbfZEBGFKJZEBFKJZABKJFEB', '300'], ['Paul', '400'], ['Jacques', '500'], ['Jean', '600'], ['Marie', '700'], ['Louise', '800'], ['Julie', '900'], ['Julien', '1000'], ['Marie', '1100'], ['Louise', '1200']]

if __name__ == "__main__":
    menugui(test_list)
