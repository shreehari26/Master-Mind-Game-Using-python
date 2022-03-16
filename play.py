import tkinter as tk
from tkinter import *
from maingame import *

def play_game():
   #create a window
   root=tk.Toplevel()
   root.title("MASTERMIND.")
   root.geometry("700x700")
   root.iconbitmap(r'brain.ico')
   # Add image file 
   bg = PhotoImage(file = "pegs.png") 
   
   # Show image using label
   
   label1 = Label(root, image = bg) 
   label1.place(x = 0, y = 0)
   
   #entry widget and label
   l1=Label(root,text='PLAYER NAME: ',font=('Showcard Gothic',25),background='navajowhite2',relief='solid',foreground='saddle brown').place(x=25,y=250)
   
   e1=Entry(root,font=('Showcard Gothic',30),relief='solid',foreground='saddle brown',width=15).place(x=300,y=250)
   
   

   
   #start game button
   root.loadimage2=PhotoImage(file="greenball2.png")
   root.greenbutton1=Button(root,image=root.loadimage2,command=main)
   root.greenbutton1["bg"]='black'
   root.greenbutton1.place(x=300,y=400)

   root.mainloop()

   

