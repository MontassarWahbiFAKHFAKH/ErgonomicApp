from ast import Lambda
from tkinter import *
from turtle import width
from PIL import Image
from tkinter import messagebox
import sys
import os
import subprocess

window=Tk()
window.title("NIOSH")
window.geometry("900x520")
window.resizable(0,0)
window.iconbitmap("./fenetre1/NIOSH/icon.ico")
window.config(bg="white")
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def open_image():
    image_1=Image.open('./fenetre1/NIOSH/Eq_NIOSH.png')
    image_1.show()

def open_image_2():
    image_2=Image.open('./fenetre1/NIOSH/angle_A.png')
    image_2.show()  

def open_image_3():
    image_3=Image.open('./fenetre1/NIOSH/Facteur FF.png')
    image_3.show()     

def open_image_4():
    image_4=Image.open('./fenetre1/NIOSH/Facteur FI.png')
    image_4.show()            

def action1(event1):
    charge=entryNombre1.get()
    if isfloat(charge)==True:
        charge=float(charge)
        if charge>=0:
            var1.set("Charge = "+str(charge)+" KG")
        else:
            var1.set("Erreur")      
    else:
        var1.set("Erreur")

def action2(event2):
    H=entryNombre2.get()
    if isfloat(H)==True:
        H=float(H)
        if 0<=H<=25:
            FH=1
            var2.set("FH = "+ str(FH))
        elif H<0:
            var2.set("Erreur")    
        else:
            FH=round((25/float(H)),2)
            var2.set("FH = "+ str(FH))    
    else:
        var2.set("Erreur")

def action3(event3):
    v=entryNombre3.get()
    if isfloat(v)==True:
        v=float(v)
        if v>=0:
            FV=round((1-0.003*abs(v-75)),2)
            var3.set("FV = "+ str(FV))
        else:
            var3.set("Erreur")       
    else:
        var3.set("Erreur") 

def action4(event4):
    D=entryNombre4.get()
    if isfloat(D)==True:
        D=float(D)
        if 0<=D<=25:
            FD=1
            var4.set("FD = "+ str(FD))
        elif D<0:
            var4.set("Erreur")
        else:
            FD=round((0.82+(4.5/D)),2)
            var4.set("FD = "+ str(FD))
    else:
        var4.set("Erreur")

def action5(event5):
    A=entryNombre5.get()
    if isfloat(A)==True:
        A=float(A)
        if A<0:
            var5.set("Erreur")
        else:
            FA=round((1-(0.0032*A)),2)
            var5.set("FA = "+ str(FA)) 
    else:
        var5.set("Erreur") 

def action6(event6):
    FF=entryNombre6.get()
    if isfloat(FF)==True:
        FF=float(FF)
        if FF<0:
            var6.set("Erreur")
        else:
            var6.set("FF = "+ str(FF))
    else:
        var6.set("Erreur")

def action7(event7):
    FI=entryNombre7.get()
    if isfloat(FI)==True:
        FI=float(FI)
        if FI==1 or FI==0.9 or FI==0.95:
            var7.set("FI = "+ str(FI))
        else:
            var7.set("Erreur")
           
    else:
        var7.set("Erreur")


def CMA(): 
    charge=entryNombre1.get()
    H=entryNombre2.get()
    D=entryNombre4.get()
    v=entryNombre3.get()
    A=entryNombre5.get()
    FF=entryNombre6.get()
    FI=entryNombre7.get()

    if(float(H)<0 or float(v)<0 or float(D)<0 or float(A)<0 or float(FF)<0 or float(FI)<0 or float(charge)<0 or (float(FI)!=1 and float(FI)!=0.95 and float(FI)!=0.90 )):
        messagebox.showerror("Resultat", "Erreur")

    elif (0<=float(H)<=25 and 0<=float(D)<=25):
        FV=round((1-0.003*abs(float(v)-75)),2)
        FA=round((1-(0.0032*float(A))),2)
        CMA=23*float(FF)*float(FI)*FV*FA
    elif (0<=float(H)<=25 and float(D)>25):
        FD=round((0.82+(4.5/float(D))),2)
        FV=round((1-0.003*abs(float(v)-75)),2)
        FA=round((1-(0.0032*float(A))),2)
        CMA=23*FV*FD*FA*float(FF)*float(FI)
    elif(0<=float(D)<=25 and float(H)>25):
        FH=round((25/float(H)),2)
        FV=round((1-0.003*abs(float(v)-75)),2)
        FA=round((1-(0.0032*float(A))),2)
        CMA=23*FV*FH*FA*float(FF)*float(FI)
    else:
        FD=round((0.82+(4.5/float(D))),2)
        FH=round((25/float(H)),2)
        FV=round((1-0.003*abs(float(v)-75)),2)
        FA=round((1-(0.0032*float(A))),2)
        CMA=23*FV*FH*FA*float(FF)*float(FI)*FD
    
    if float(charge)>CMA:
        messagebox.showinfo("Resultat","La charge maximale admissible CMA = {0} KG < {1} KG \n Cette tache est dangereuse et susceptible d'augmenter le risque de blessures associ\xe9es au levage.".format(round(CMA,2),float(charge)))
    elif float(charge)==CMA:
        messagebox.showinfo("Resultat","La charge maximale admissible CMA = {0} KG = {1} KG \n Cette tache est dangereuse et susceptible d'augmenter le risque de blessures associ\xe9es au levage.".format(round(CMA,2),float(charge)))
    else:
        messagebox.showinfo("Resultat","La charge maximale admissible CMA = {0} KG > {1} KG \n Cette tache n'est pas dangereuse et peut etre accomplie en toute s\xe9curit\xe9.".format(round(CMA,2),float(charge)))

def quitter():
    window.destroy()   

def precedent():
    window.destroy()
    subprocess.call("python ./fenetre1/fenetre_1.py",shell=True)
    
label_0=Label(window,text="Remplir les cases suivantes :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_0.pack()
label_0.place(relx=0.5,y=30,anchor=CENTER)         
    
lblnombre1=Label(window, text="Entrer la charge a lever en kg :",bg="white",activebackground="white")
lblnombre1.place(x=40,y=88)
entryNombre1=Entry(window)
entryNombre1.place(x=220,y=90)
entryNombre1.bind('<Return>',action1)
Result1=Label(window,textvariable=var1,bg="white")
Result1.place(x=380,y=90)

image=PhotoImage(file="./fenetre1/NIOSH/Eq_NIOSH.png")
labelimage=Label(image=image)
labelimage.place(x=480,y=70)


lblnombre2=Label(window, text="Entrer la distance  H en cm :",bg="white",activebackground="white")
lblnombre2.place(x=40,y=140)
entryNombre2=Entry(window)
entryNombre2.place(x =220,y=142)
entryNombre2.bind('<Return>',action2)
Result2=Label(window,textvariable=var2,bg="white")
Result2.place(x=380,y=142)


lblnombre3=Label(window, text="Entrer la distance  V en cm :",bg="white",activebackground="white")
lblnombre3.place(x=40,y=192)
entryNombre3=Entry(window)
entryNombre3.place(x =220,y=194)
entryNombre3.bind('<Return>',action3)
Result3=Label(window,textvariable=var3,bg="white")
Result3.place(x=380,y=194)



lblnombre4=Label(window, text="Entrer la distance  D en cm :",bg="white",activebackground="white")
lblnombre4.place(x=40,y=244)
entryNombre4=Entry(window)
entryNombre4.place(x =220,y=246)
entryNombre4.bind('<Return>',action4)
Result4=Label(window,textvariable=var4,bg="white")
Result4.place(x=380,y=246)



lblnombre5=Label(window, text="Entrer l'angle  A en degr\xe9 :",bg="white",activebackground="white")
lblnombre5.place(x=40,y=296)
entryNombre5=Entry(window)
entryNombre5.place(x =220,y=298)
entryNombre5.bind('<Return>',action5)
Result5=Label(window,textvariable=var5,bg="white")
Result5.place(x=380,y=298)

telechargement1=PhotoImage(file="./fenetre1/NIOSH/telechargement.png")
button_2=Button(window,image=telechargement1,width=23,height=23,command=open_image_2,border="0",bg="white",activebackground="white")
button_2.pack()
button_2.place(x=10,y=291)


lblnombre6=Label(window, text="Entrer le facteur FF :",bg="white",activebackground="white")
lblnombre6.place(x=40,y=348)
entryNombre6=Entry(window)
entryNombre6.place(x =220,y=350)
entryNombre6.bind('<Return>',action6)
Result6=Label(window,textvariable=var6,bg="white")
Result6.place(x=380,y=350)

telechargement3=PhotoImage(file="./fenetre1/NIOSH/telechargement.png")
button_3=Button(window,image=telechargement3,width=23,height=23,command=open_image_3,border="0",bg="white",activebackground="white")
button_3.pack()
button_3.place(x=10,y=344)

lblnombre7=Label(window, text="Entrer le facteur FI :",bg="white",activebackground="white")
lblnombre7.place(x=40,y=400)
entryNombre7=Entry(window)
entryNombre7.place(x =220,y=402)
entryNombre7.bind('<Return>',action7)
Result7=Label(window,textvariable=var7,bg="white")
Result7.place(x=380,y=402)

telechargement4=PhotoImage(file="./fenetre1/NIOSH/telechargement.png")
button_4=Button(window,image=telechargement4,width=23,height=23,command=open_image_4,border="0",bg="white",activebackground="white")
button_4.pack()
button_4.place(x=10,y=397)

telechargement_check=PhotoImage(file="./fenetre1/NIOSH/check.png")
button_1=Button(window,image=telechargement_check,fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=CMA)
button_1.pack()
button_1.place(relx=0.5,y=480,anchor=CENTER)


telechargement_precedent=PhotoImage(file="./fenetre1/NIOSH/precedent.png")
button_2=Button(window,image=telechargement_precedent,fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=precedent)
button_2.pack()
button_2.place(x=100,y=450)

telechargement_quitter=PhotoImage(file="./fenetre1/NIOSH/quitter.png")
button_3=Button(window,image=telechargement_quitter,fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=quitter)
button_3.pack()
button_3.place(x=749,y=450)

window.mainloop()

