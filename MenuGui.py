from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from config import get_scoreboard

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

def relative_to_assets(path: str) -> Path:
    #Redirige le chemin vers le dossier assets (prévient les erreurs de chemin, Windows hihihi)
    return ASSETS_PATH / Path(path)

class MenuGui: 
    def choicelevel(self, event) :
        #Cette fonction est appelée quand on clique sur un élément de la Combobox
        #Elle permet de récupérer la valeur sélectionnée
        #et de l'afficher dans la console
        print("Changing level to " + self.combobox.get())
        self.choicedlevel = self.combobox.get()
        
        if self.choicedlevel == "Facile (10x10 - 8 trésors)":
            self.choicedlevel = 1
        elif self.choicedlevel == "Moyen (20x24 - 10 trésors)":
            self.choicedlevel = 2
        elif self.choicedlevel == "Difficile (24x36 - 12 trésors)":
            self.choicedlevel = 3
        elif self.choicedlevel == "Configuration personnalisée":
            self.choicedlevel = 4
        self.window.destroy()
        MenuGui(self.choicedlevel)
        

    def __init__(self, level):

        self.window = Tk()
        self.window.geometry("1004x565")
        self.window.title("Treasure Hunter (build 1.0.8)")
        self.window.configure(bg = "#FFFFFF")

        

        self.parameters = get_scoreboard(level)

        self.list = self.parameters[0]
        self.level = self.parameters[1]

        print(self.list)
        print(self.level)


        #Création du canvas
        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 565,
            width = 1004,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        ###############################################################
        #LES IMAGES (crées précédements avec GIMP + Figma)

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            502.0,
            282.0,
            image=image_image_1
        )
        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            806.0,
            78.0,
            image=image_image_2
        )


        ###############################################################
        #LES BOUTONS

        #Lancer la partie
        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.launch(),
            relief="flat"
        )
        self.button_1.place(
            x=45.0,
            y=428.0,
            width=288.0,
            height=92.0
        )

        #Configuration expert
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.expert(),
            relief="flat"
        )
        self.button_2.place(
            x=360.0,
            y=431.0,
            width=230.0,
            height=87.0
        )
        ###############################################################
        #LES ENTRÉES (pour les pseudos)
        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            396.5,
            167.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=223.0,
            y=151.0,
            width=347.0,
            height=31.0
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            396.5,
            231.5,
            image=entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=223.0,
            y=215.0,
            width=347.0,
            height=31.0
        )

        entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            438.0,
            307.5,
            image=entry_image_3
        )

        
        self.level_list=["Facile (10x10 - 8 trésors)", "Moyen (20x24 - 10 trésors)", "Difficile (24x36 - 12 trésors)", "Configuration personnalisée"]
        import tkinter.ttk as ttk
        self.combobox = ttk.Combobox(
            self.window,
            values=self.level_list
        )

        self.combobox.current(0)
        self.combobox.place(
            x=306.0,
            y=291.0,
            width=264.0,
            height=31.0
        )
        self.combobox.config(state="readonly")

        #la combobox est par défaut sur le choix donné
        self.combobox.set(self.level_list[self.level - 1])

        self.combobox.bind("<<ComboboxSelected>>", self.choicelevel)


        # self.entry_3 = Entry(
        #     bd=0,
        #     bg="#FFFFFF",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_3.place(
        #     x=306.0,
        #     y=291.0,
        #     width=264.0,
        #     height=31.0
        # )

        ###############################################################

        #SCOREBOARD

        #si la liste est vide, on renvoie rien
        if self.list == []:
            return None
        #si la liste dépasse 12 scores, on ne prend que les 12 premiers (par je ne sais quel miracle ahh)
        if len(self.list) > 12:
            list = list[:12]
        #si la liste contient au moins un pseudo, on crée son texre
        for i in range(0, len(self.list)):
            self.canvas.create_text(
                666.0,
                143.0 + (29 * i),
                anchor="nw",
                text=self.list[i][0],
                fill="#FFFFFF",
                font=("PiecesofEight", 20 * -1)
                
                )

        #même chose pour les scores

        #si la liste est vide, on renvoie rien
        if self.list == []:
            return None
        #si la liste dépasse 12 scores, on ne prend que les 12 premiers (au cas où, on ne sait jamais lol)
        if len(self.list) > 12:
            self.list = self.list[:12]
        #si la liste contient au moins un score, on crée le texte correspondant
        for i in range(0, len(self.list)):
            self.canvas.create_text(
            895.0,
            143.0 + (29 * i),
            anchor="nw",
            text=self.list[i][1],
            fill="#FFFFFF",
            font=("PiecesofEight", 20 * -1)
            
            )

        self.window.resizable(False, False)
        self.window.mainloop()

    def expert(self) :
        #une alerte tkinter pour dire que c'est en cours
        self.window.destroy()
        from ExpertGui import Expertgui
        Expertgui()

    def launch(self) :
        print("Saving configuration...")
        #A FINIR
        print("Starting game...")
        #self.window.destroy()
        from JeuGui import JeuGui
        JeuGui()
        #Une alerte tkinter pour dire que c'est en cours
        
        #self.window.messagebox.showinfo("En cours de développement, ça arrive :)")




