from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/leo/Documents/GitHub/TreasureHunter/build/assets/frame1")


def relative_to_assets(path: str) -> Path:
    #Redirige le chemin vers le dossier assets (prévient les erreurs de chemin, Windows ahhhh)
    return ASSETS_PATH / Path(path)




def run_expert():

    window = Tk()
    window.geometry("663x497")
    window.title("Treasure Hunter (build 1.0.8) (expert configuration mode)")
    window.configure(bg = "#FFFFFF")
    window.resizable(False, False)
    #On crée le canvas

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 497,
        width = 663,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        331.0,
        248.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("ça va arriver bientôt... hihi"),
        relief="flat"
    )
    button_1.place(
        x=230.0,
        y=396.0,
        width=207.0,
        height=62.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        395.0,
        226.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=195.0,
        y=210.0,
        width=400.0,
        height=31.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        404.0,
        284.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=213.0,
        y=269.0,
        width=382.0,
        height=29.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        438.0,
        336.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=281.0,
        y=321.0,
        width=314.0,
        height=29.0
    )
    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    run_expert()
