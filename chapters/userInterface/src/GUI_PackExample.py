# gui/GUI_PackExample.py
# Listbox Beispiel im Pack-Manager

from tkinter import *

root = Tk()

listbox = Listbox(root)
listbox.pack()

for i in range(20):
    listbox.insert(END, str(i))

mainloop()
