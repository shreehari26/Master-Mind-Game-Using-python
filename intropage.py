import tkinter as tk
from tkinter import *
from play import *
from help_g import *


#creating a window
intro=tk.Tk()
intro.title("MASTERMIND.")
intro.geometry("700x700")
intro.iconbitmap(r'brain.ico') 
# Add image file 
bg = PhotoImage(file = "mastermind2.png") 
  
# Show image using label

label1 = Label( intro, image = bg) 
label1.place(x = 0, y = 0)
#label
l1=Label(intro,text='MASTERMIND',font=('Showcard Gothic',35),background='navajowhite2',relief='solid',foreground='saddle brown').pack(pady=200)
#Buttons for PLAY and HELP
intro.loadimage=PhotoImage(file="redball2.png")
intro.bluebutton=Button(intro,image=intro.loadimage,command=play_game)
intro.bluebutton["bg"]='black'
intro.bluebutton.place(x=600,y=450)

intro.loadimage1=PhotoImage(file="blueball2.png")
intro.bluebutton1=Button(intro,image=intro.loadimage1,command=gamehelp)
intro.bluebutton1["bg"]='black'
intro.bluebutton1.place(x=600,y=550)


intro.mainloop()
