import os
from pathlib import Path
from tkinter import END, Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("500x500")
window.configure(bg = "#742C58")

def confirmBut(entry1, entry2, entry3):
    year = entry1.get()
    paperNum = entry2.get()
    invalid = False
    if not str.isdigit(year) or not str.isdigit(paperNum):
        invalid = True
    elif len(year) != 4  or len(paperNum) != 2:
        invalid = True
    if invalid: 
        entry_3.delete('1.0', END)
        entry3.insert(END, 'Unexpected Input.')
    else:
        f = open('logs.txt', 'a')
        f.write(' ' + year + ' ' + paperNum)
        f.close()
        window.destroy()
        os.system('python reqmak/request-making.py')

canvas = Canvas(
    window,
    bg = "#742C58",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    114.0,
    121.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_1.place(
    x=33.0,
    y=102.0,
    width=162.0,
    height=37.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    375.0,
    121.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_2.place(
    x=294.0,
    y=102.0,
    width=162.0,
    height=37.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    250.0,
    488.0,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_3.place(
    x=0.0,
    y=476.0,
    width=500.0,
    height=22.0
)

canvas.create_text(
    33.0,
    80.0,
    anchor="nw",
    text="Year:",
    fill="#FFFFFF",
    font=("JostRoman Regular", 16 * -1)
)

canvas.create_text(
    294.0,
    80.0,
    anchor="nw",
    text="Paper Number:",
    fill="#FFFFFF",
    font=("JostRoman Regular", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: confirmBut(entry1=entry_1, entry2=entry_2, entry3=entry_3),
    relief="flat"
)
button_1.place(
    x=186.0,
    y=234.0,
    width=139.0,
    height=33.0
)
entry_3.bind("<Key>", lambda e: "break")
window.resizable(False, False)
window.mainloop()
