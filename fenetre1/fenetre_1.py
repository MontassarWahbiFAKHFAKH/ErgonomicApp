from ast import Lambda
import os
from tkinter import *
from PIL import Image
import sys
import subprocess

def selection():
        selection=radio.get()
        if selection==1:
            window.destroy()
            subprocess.call("python ./fenetre1/RULA/RULA.py",shell=True)
        elif selection==2:
            window.destroy()
            subprocess.call("python ./fenetre1/REBA/REBA.py",shell=True)
        elif selection==3:
            window.destroy()
            subprocess.call("python ./fenetre1/NIOSH/NIOSH.py",shell=True)
            
               
def quitter():
    window.destroy()
 


def press(event):
    a=event.keysym
    if a=="Return":
        selection()

window=Tk()
radio=IntVar()
window.title("Evaluation ergonomique des postures de travail")
window.geometry("900x520")
window.iconbitmap("./fenetre1/icon.ico")
window.resizable(0,0)

window.config(bg="white")
label_1=Label(window,text="Bienvenue",font=("Times New Roman",30),fg="#1E90FF",bg="white",activebackground="white")
label_1.pack(pady=10)
label_2=Label(window,text="Choisir la m\xe9thode convenable avec votre application :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_2.pack(pady=30)
value=StringVar()
b1=Radiobutton(window, text="RULA (Rapid Upper Limb Assessment)",font=("Times New Roman",20),fg="black",var=radio,value=1,bg="white",activebackground="white")
b2=Radiobutton(window, text="REBA (Rapid Entire Body Assessment)",font=("Times New Roman",20),fg="black",var=radio,value=2,bg="white",activebackground="white") 
b3=Radiobutton(window, text="NIOSH                                                  ",font=("Times New Roman",20),fg="black",var=radio,value=3,bg="white",activebackground="white") 
b1.pack(pady=8)
b2.pack(pady=8)
b3.pack(pady=8)

telechargement_enter=PhotoImage(file="./fenetre1/enter.png")
button_1=Button(window,image=telechargement_enter,fg="white",width=60,height=60,bg="white",activebackground="white",border="0",command=selection)
button_1.pack()
button_1.place(x=300,y=380)
button_1.bind_all('<Key>',press)
telechargement_quitter=PhotoImage(file="./fenetre1/quitter.png")
button_2=Button(window,image=telechargement_quitter,fg="white",width=60,height=60,bg="white",activebackground="white",border="0",command=quitter)
button_2.pack()
button_2.place(x=500,y=380)



window.mainloop()
