from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1000x700")
#Style
#style = ttk.Style()
#style.configure("TButton", font="Serif 15 bold", padding=10, foreground="red")

window = ttk.Frame(root, padding=10)
window.grid()


ttk.Button(window, text="Quit", command=root.destroy).grid(row=0, column=3)

#variables
money = 1000





#Boom Button
ttk.Label(window, text="Money: "+str(money)).grid(row=0, column=0)
ttk.Button(window, text="Boom").grid(row=1, column=0)
ttk.Button(window, text="Up").grid(row=2, column=0)
ttk.Button(window, text="Down").grid(row=3, column=0)
ttk.Button(window, text="Spin").grid(row=3, column=3)










root.mainloop()