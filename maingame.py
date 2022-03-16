import tkinter as tk
from tkinter import *
import random
from functools import partial

def main():
   n = 10   #this is the length of the list l
   lngt = 900 // 15 #this is the dimension of the squares that I want

   root= tk.Toplevel()
   root.geometry("800x800")
   root.title("MASTERMIND.")
   root.iconbitmap('brain.ico')
   root.configure(background='lightblue')

   #I would like to create a table of 4 rows on canvas
   #each row should contain 4 squares
   can =Canvas(root, width=800, height=800,bg='tomato2')
   can.pack(side=LEFT)

   for i in range(n):
       y = i * lngt
       for j in range(4):
           x = j * lngt
           can.create_rectangle(x, y, x+lngt, y+lngt, fill="wheat1")
   orde=0
   x0=10
   x1=50
   y0=10
   y1=50

   st=[]
   trial=1

   comp_generated=random.sample('brpgyon',4)
   print(comp_generated)



   #functions
   def xyz(i_l):
       nonlocal x0,x1,y0,y1,trial,st,comp_generated
       x0=250
       x1=290
    
       if i_l==comp_generated:
           ss=Label(root,text='YOU DID IT',bg='Gold',font=('Showcard Gothic',30)).place(x=300,y=300)
        
       elif trial==10:
           ss=Label(root,text='Game Over',bg='Gold',font=('Showcard Gothic',30)).place(x=300,y=300)
           root.after(8000, lambda: root.destroy())
       else:
           ss=Label(root,text='Try Again',bg='Gold',font=('Showcard Gothic',30))
           ss.place(x=300,y=300)
           root.after(1000,ss.destroy)
        
           for i in range(0,4):
    
               if i_l[i] in comp_generated:
                   if i_l[i]==comp_generated[i]:
                      # print(l.index(i),i_l.index(i))
                       can.create_oval(x0,y0,x1,y1,fill='grey1')
                       x0+=60
                       x1+=60
                   else:
                       can.create_oval(x0,y0,x1,y1,fill='snow')
                       x0+=60
                       x1+=60
           x0=10
           x1=50

    
                        
       st*=0
       trial+=1
       y1+=60
       y0+=60
    
   def standby(col):
       nonlocal x0,x1,y0,y1,orde,st
       st.append(col)
       if orde==4:
          root.Click=PhotoImage(file='click.png') 
          b=Button(root,image=root.Click,command=partial(xyz,st),bg='tomato2').place(x=680,y=500)
          orde=0
       else:
            pass
    
        
   def g1():
      nonlocal orde
      orde+=1
      nonlocal x0,x1,y0,y1
      can.create_oval(x0,y0,x1,y1,fill='royal blue')
      x0+=60
      x1+=60
      return standby('b')
   def g2():
      nonlocal orde
      orde+=1
      nonlocal x0,x1,y0,y1
      can.create_oval(x0,y0,x1,y1,fill='red3')
      x0+=60
      x1+=60
      return standby('r')
   def g3():
      nonlocal orde
      orde+=1
      nonlocal x0,x1,y0,y1
      can.create_oval(x0,y0,x1,y1,fill='magenta4')
      x0+=60
      x1+=60
      return standby('p')
   def g4():
      nonlocal orde
      orde+=1
      nonlocal x0,x1,y0,y1
      can.create_oval(x0,y0,x1,y1,fill='olive drab')
      x0+=60
      x1+=60
      return standby('g')
   def g5():
      nonlocal orde
      orde+=1
      nonlocal x0,x1,y0,y1
      can.create_oval(x0,y0,x1,y1,fill='gold2')
      x0+=60
      x1+=60
      return standby('y')
   def g6():
      nonlocal orde
      orde+=1
      nonlocal x0,x1,y0,y1
      can.create_oval(x0,y0,x1,y1,fill='orange red')
      x0+=60
      x1+=60
      return standby('o')
   def g7():
      nonlocal orde
      orde+=1
      nonlocal x0,x1,y0,y1
      can.create_oval(x0,y0,x1,y1,fill='saddle brown')
      x0+=60
      x1+=60
      return standby('n')

    
#1
   root.loadimage1=PhotoImage(file="1b.png")
   root.roundedbutton1=Button(root,image=root.loadimage1,command=g1)
   root.roundedbutton1["bg"]='black'
   root.roundedbutton1.place(x=700,y=150)
#2
   root.loadimage2=PhotoImage(file="2r.png")
   root.roundedbutton2=Button(root,image=root.loadimage2,command=g2)
   root.roundedbutton2["bg"]='black'
   root.roundedbutton2.place(x=700,y=200)
#3
   root.loadimage3=PhotoImage(file="3p.png")
   root.roundedbutton3=Button(root,image=root.loadimage3,command=g3)
   root.roundedbutton3["bg"]='black'
   root.roundedbutton3.place(x=700,y=250)
#4
   root.loadimage4=PhotoImage(file="4g.png")
   root.roundedbutton4=Button(root,image=root.loadimage4,command=g4)
   root.roundedbutton4["bg"]='black'
   root.roundedbutton4.place(x=700,y=300)
#5
   root.loadimage5=PhotoImage(file="5y.png")
   root.roundedbutton5=Button(root,image=root.loadimage5,command=g5)
   root.roundedbutton5["bg"]='black'
   root.roundedbutton5.place(x=700,y=350)
#6
   root.loadimage6=PhotoImage(file="6o.png")
   root.roundedbutton6=Button(root,image=root.loadimage6,command=g6)
   root.roundedbutton6["bg"]='black'
   root.roundedbutton6.place(x=700,y=400)
#7
   root.loadimage7=PhotoImage(file="7br.png")
   root.roundedbutton7=Button(root,image=root.loadimage7,command=g7)
   root.roundedbutton7["bg"]='black'
   root.roundedbutton7.place(x=700,y=450)
#MASTERMIND
   l=Label(root,text='MASTERMIND',font=('Bernard MT Condensed','80'),bg='tomato2',fg='Black').place(x=150,y=650)


   root.mainloop()
