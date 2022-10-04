import os
import tkinter as tk

def sel():
    val = ['qp', 'ms', 'in', 'gt']
    f = open('logs.txt', 'a')
    f.write(' ' + str(val[var.get()-1]))
    root.destroy()
    f.close()
    os.system('python finalinfo/finalinfo.py')

root = tk.Tk()
root.geometry('300x200')

tk.Label(root, 
        text="""Choose the required examination paper type:""",
        justify = tk.LEFT,
        padx = 20).pack()

var = tk.IntVar()
R1 = tk.Radiobutton(root, text="qp", variable=var, value=1,
                  command=sel)
R1.pack( anchor = tk.CENTER)

R2 = tk.Radiobutton(root, text="ms", variable=var, value=2,
                  command=sel)
R2.pack( anchor = tk.CENTER )

R3 = tk.Radiobutton(root, text="in", variable=var, value=3,
                  command=sel)
R3.pack( anchor = tk.CENTER )

R4 = tk.Radiobutton(root, text="gt", variable=var, value=4,
                  command=sel)
R4.pack( anchor = tk.CENTER )
label = tk.Label(root)
label.pack(anchor=tk.N)

root.resizable(False, False)
root.mainloop()
