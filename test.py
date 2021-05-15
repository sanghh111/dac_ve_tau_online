from tkinter import *

def onClick(i):
   print(i)

master = Tk()
for i in range(2):
   Radiobutton(master,value=i,variable=IntVar(),command=lambda:onClick(i)).pack()
master.mainloop()
