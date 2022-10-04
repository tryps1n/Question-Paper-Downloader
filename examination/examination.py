from concurrent.futures import thread
import pathlib
from pathlib import Path
from threading import Thread
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Olev(window):
    f = open('logs.txt', 'w')
    f.write('O')
    f.close()
    window.destroy()
    os.system('python subselec/subselec.py')

window = Tk()

window.geometry("750x600")
window.configure(bg = "#808F54")

canvas = Canvas(
    window,
    bg = "#808F54",
    height = 600,
    width = 750,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    218.0,
    143.0,
    anchor="nw",
    text="Select Examination",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Olev(window=window),
    relief="flat"
)
button_1.place(
    x=205.0,
    y=329.0,
    width=340.0,
    height=48.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=205.0,
    y=491.0,
    width=340.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()

