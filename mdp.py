from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from dotenv import load_dotenv
import os

window=Tk()
window.geometry('360x500')
window.title('Se connecter')
window.resizable(0,0)
window.iconbitmap("icon.ico")


def press(event):
    a=event.keysym
    if a=="Return":
        cmd()           
j=0
r=0
for i in range(100):
    c=str(222222+r)
    Frame (window, width=10,height=500, bg='#'+c).place(x=j,y=0)
    j=j+10
    r=r+1
Frame(window, width=260, height=400, bg='white').place(x=50,y=50)
#label
l1=Label(window,text="Nom d'utilisateur",bg="white")
l=("consolas",13) #font,text size
l1.config(font=1)
l1.place(x=80,y=200)

e1=Entry(window,width=20, border=0)
e1.config(font=1)
e1.place(x=80,y=230)

#label2
l2=Label(window,text="Mot de passe",bg="white")
l=("consolas",13) #font, text size
l2.config(font=1)
l2.place(x=80,y=280)

e2=Entry(window,width=20,border=0,show="*")
e2.config(font=1)
e2.place(x=80,y=310)

Frame(window,width=180, height=2, bg="#141414").place(x=80,y=250)
Frame(window,width=180, height=2, bg="#141414").place(x=80,y=330)

imagel=Image.open("log.png")
image2=ImageTk. PhotoImage(imagel)
label1=Label(image=image2, border=0, justify=CENTER,bg="white")
label1.place(relx=0.5,y=130,anchor=CENTER)


load_dotenv()
login = os.getenv('LOGIN')
mdp = os.getenv('MDP')

def cmd():
    if e1.get()==login and e2.get()==mdp:
        window.destroy()
        from fenetre1 import fenetre_1
    elif e1.get()==login and e2.get()!=mdp:
        messagebox.showinfo("Connexion echouée"," Mot de passe incorrect ")
    elif e1.get()!=login and e2.get()==mdp:
        messagebox.showinfo("Connexion echouée"," Nom d'utilisateur incorrect ") 
    else:
        messagebox.showinfo("Connexion echouée"," Nom d'utilisateur incorrect ")      
button=Button(window, width=20, height=2, fg='white', bg='#994422', border=0, command=cmd, text="VALIDER")
button.place(x=100, y=375)
button.bind_all('<Key>',press)

window.mainloop()
