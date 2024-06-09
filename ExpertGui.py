from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Scale, HORIZONTAL, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame1")


def relative_to_assets(path: str) -> Path:
    #Redirige le chemin vers le dossier assets (prévient les erreurs de chemin, Windows ahhhh)
    return ASSETS_PATH / Path(path)


class Expertgui:

    def __init__(self) -> None:
        self.window = Tk()
        self.window.geometry("663x497")
        self.window.title("Treasure Hunter (build 1.0.8) (expert configuration mode)")
        self.window.configure(bg = "#FFFFFF")
        self.window.resizable(False, False)
        #On crée le canvas

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 497,
            width = 663,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        #L'image de fond
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            331.0,
            248.0,
            image=self.image_image_1
        )

        #Le bouton de sauvegarde

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.save(),
            relief="flat"
        )
        self.button_1.place(
            x=230.0,
            y=396.0,
            width=207.0,
            height=62.0
        )


        #Le slider de ligne

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            395.0,
            226.5,
            image=self.entry_image_1
        )

        w2 = Scale(self.window, from_=1, to=32, length=400, orient=HORIZONTAL)
        w2.set(15)

        self.entry_1 = self.canvas.create_window(395.0, 226.5, window=w2)

       
        # self.entry_1 = Entry(
        #     bd=0,
        #     bg="#FFFFFF",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_1.place(
        #     x=195.0,
        #     y=210.0,
        #     width=400.0,
        #     height=31.0
        # )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            404.0,
            284.5,
            image=self.entry_image_2
        )

        w3 = Scale(self.window, from_=1, to=32, length=382.0, orient=HORIZONTAL)
        w3.set(15)

        self.entry_2 = self.canvas.create_window(404.0, 284.5, window=w3)

        # self.entry_2 = Entry(
        #     bd=0,
        #     bg="#FFFFFF",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_2.place(
        #     x=213.0,
        #     y=269.0,
        #     width=382.0,
        #     height=29.0
        # )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            438.0,
            336.5,
            image=self.entry_image_3
        )

        w4 = Scale(self.window, from_=1, to=32, length=314.0, orient=HORIZONTAL)
        w4.set(15)
        self.entry_3 = self.canvas.create_window(438.0, 336.5, window=w4)


        # self.entry_3 = Entry(
        #     bd=0,
        #     bg="#FFFFFF",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_3.place(
        #     x=281.0,
        #     y=321.0,
        #     width=314.0,
        #     height=29.0
        # )
        self.window.resizable(False, False)
        self.window.mainloop()

    def save(self) :
        #EN COURS
        #Enregistre (get les sliders et les textboxes) et modifie le fichier de configuraiton
        print("Sauvegarde en cours d'implémentation...")

        messagebox.showwarning(title = "Attention", message = "Pour utiliser les paramètres personnalisés, veuillez veiller à choisir « Personnalisé » dans le menu déroulant")
        

        #on détruit la fenêtre de config
        self.window.destroy()
        
        from MenuGui import MenuGui

        MenuGui([["J1", "0"], ["J2", "0"], ["J3", "0"], ["J4", "0"], ["J5", "0"], ["J6", "0"], ["J7", "0"], ["J8", "0"], ["J9", "0"], ["J10", "0"], ["J11", "0"], ["J12", "0"]])

