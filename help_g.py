import tkinter as tk
from tkinter import *


def gamehelp():
#creating a window
   rules=tk.Toplevel()
   rules.title("MASTERMIND.")
   rules.geometry("700x700")
   rules.iconbitmap(r'brain.ico')
   rules.config(bg="grey")
# Add image file 
   bg = PhotoImage(file = "questionmark.png") 
   
# Show image using label
   
   label1 = Label(rules, image = bg) 
   label1.place(x = 0, y = 0)
   
   r1="1. The computer will auto generate the code."
   r2="\n2. The code is made up of any combination of the coloured pegs."
   r3="\n3. The code can be made up of any combination of the coloured pegs."
   r4="\n4. Once the code is set,you can begin guessing,"
   r5="try to guess the exact colours and positions of the hidden Code pegs."
   r6='\n5. Each guess is made by clicking the colours in the color palette.'
   r7="\n6.After every guess, the computer will inform your progress using the Black and White pegs as follows:\nBlack peg Indicates:\nBlack peg displays the number of pegs that are the correct colours in the correct position\nWhite Peg indicates:\nWhite pegs display correct coloured pegs but incorrect position." 

   label2=Label(rules,text='RULES',font=('Showcard Gothic',35),background="navajo white",foreground='DarkGoldenrod2').pack()
   l1=Label(rules,text=r1,font=('Showcard Gothic',10),background="RosyBrown1",foreground='black').place(x=0,y=70)
   l2=Label(rules,text=r2,font=('Showcard Gothic',10),background="RosyBrown1",foreground='black').place(x=0,y=120)
   l3=Label(rules,text=r3,font=('Showcard Gothic',10),background="RosyBrown1",foreground='black').place(x=0,y=170)
   l4=Label(rules,text=r4,font=('Showcard Gothic',10),background="RosyBrown1",foreground='black').place(x=0,y=220)
   l5=Label(rules,text=r5,font=('Showcard Gothic',10),background="RosyBrown1",foreground='black').place(x=0,y=270)   
   l6=Label(rules,text=r6,font=('Showcard Gothic',10),background="RosyBrown1",foreground='black').place(x=0,y=320)
   l7=Label(rules,text=r7,font=('Showcard Gothic',9),background="RosyBrown1",foreground='black').place(x=0,y=370)
   rules.mainloop()

