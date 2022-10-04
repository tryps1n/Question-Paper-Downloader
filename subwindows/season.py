import os
import tkinter as tk

root = tk.Tk()

def sel():
    val = ['s', 'w']
    f = open('logs.txt', 'a')
    f.write(' ' + str(val[v.get()-1]))
    root.destroy()
    f.close()
    os.system('python subwindows/papertype.py')


v = tk.IntVar()

tk.Label(root, 
        text="""Choose the required examination season:""",
        justify = tk.LEFT,
        padx = 20).pack()

tk.Radiobutton(root, 
               text="Summer (s)",
               padx = 20, 
               variable=v, 
               command=sel,
               value=1).pack(anchor=tk.W)

tk.Radiobutton(root, 
               text="Winter (W)",
               padx = 20, 
               variable=v, 
               command=sel,
               value=2).pack(anchor=tk.W)

root.resizable(False, False)
root.mainloop()
