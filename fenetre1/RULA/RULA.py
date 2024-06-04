from ast import Lambda
from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import csv
import os
import sys
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import math
import subprocess

window = Tk()
window.title("RULA (Rapid Upper Limb Assessment)")
alto=520
ancho=900
anchoalto="900x520"
window.geometry(anchoalto)
window.resizable(0,0)
window.iconbitmap("./fenetre1/RULA/icon.ico")
window.config(bg="white")
radio_1=IntVar()
radio_2=BooleanVar()
radio_3=BooleanVar()
radio_4=BooleanVar()
radio_5=IntVar()
radio_6=BooleanVar()
radio_7=IntVar()
radio_8=BooleanVar()
radio_9=IntVar()
radio_10=IntVar()
radio_11=BooleanVar()
radio_12=IntVar()
radio_13=BooleanVar()
radio_14=BooleanVar()
radio_15=IntVar()
radio_16=BooleanVar()
radio_17=BooleanVar()
radio_18=IntVar()
radio_19=IntVar()
radio_20=BooleanVar()


# Create A Main Frame
main_frame = Frame(window,width=ancho,height=alto)
main_frame.place(x=0,y=0)
# Create A Canvas
my_canvas = Canvas(main_frame, width=ancho, height=alto)
my_canvas.place(x=0,y=0)
# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.place(x=880,y=0,height=alto)
# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
def _on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas,width=ancho,height=alto,bg="white")
second_frame.place(x=0,y=0)
# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")


def TABLE_A_RULA(Etape_1_RULA,Etape_2_RULA,Etape_3_RULA,Etape_4_RULA,l_1):
    Ligne1_RULA=Etape_2_RULA+(Etape_1_RULA*2)+(Etape_1_RULA-2)
    Resultat1_RULA=l_1[Ligne1_RULA][Etape_4_RULA+(2*Etape_3_RULA-1)]
    return(Resultat1_RULA)

def TABLE_B_RULA(Etape_9_RULA,Etape_10_RULA,Etape_11_RULA,data_2_RULA):
    Ligne2_RULA=Etape_9_RULA+1
    Resultat2_RULA=data_2_RULA[Ligne2_RULA][Etape_11_RULA+(2*Etape_10_RULA-2)]
    return(Resultat2_RULA)

def TABLE_C_RULA(Etape_8_RULA,Etape_15_RULA,data_3_RULA):
    Ligne3_RULA=Etape_8_RULA
    if Etape_8_RULA>8:
        Ligne3_RULA=8
    colone_RULA=Etape_15_RULA
    if Etape_15_RULA>7:
        colone_RULA=7
    Resultat3_RULA=data_3_RULA[Ligne3_RULA][colone_RULA]
    return(Resultat3_RULA)    

def com_RU1():
    ru_1=radio_1.get()
    if ru_1==1:
        a=1
    elif ru_1==2 or ru_1==3:
        a=2 
    elif ru_1==4:
        a=3
    elif ru_1==5:
        a=4
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position de l'epaule.")    
    return(a)


def com_RU1_Ajust():
    ru_1_Ajust1=radio_2.get()
    ru_1_Ajust2=radio_3.get()
    ru_1_Ajust3=radio_4.get()

    if ru_1_Ajust1==True and ru_1_Ajust2==False and ru_1_Ajust3==False :
        b=-1
    elif (ru_1_Ajust1==False and ru_1_Ajust2==True and ru_1_Ajust3==False) or (ru_1_Ajust1==False and ru_1_Ajust2==False and ru_1_Ajust3==True) or (ru_1_Ajust1==True and ru_1_Ajust2==True and ru_1_Ajust3==True):
        b=1
    elif (ru_1_Ajust1==True and ru_1_Ajust2==True and ru_1_Ajust3==False)or(ru_1_Ajust1==True and ru_1_Ajust2==False and ru_1_Ajust3==True ) or (ru_1_Ajust1==False and ru_1_Ajust2==False and ru_1_Ajust3==False) :
        b=0
    else: 
        b=2 
    return(b)    

def SE_1():
    a=com_RU1()
    b=com_RU1_Ajust()
    if(a==1)and(b==-1):
        messagebox.showerror("Erreur", "La somme du score de la position de l'épaule avec le score de l'ajustement de la position de l'épaule ne peut pas etre egal a 0.") 
    else:    
        c=a+b
        return(c)

def com_RU2():
    ru_2=radio_5.get()
    if ru_2==1 or ru_2==3:
        a=2
    elif ru_2==2:
        a=1
    else:   
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position du coude.")  
    return(a)

def com_RU2_Ajust():
     ru_2_Ajust1=radio_6.get()    
     if ru_2_Ajust1==True:
         b=1
     else:
         b=0
     return(b)     

def SE_2():
    a=com_RU2()
    b=com_RU2_Ajust()
    c=a+b
    return(c)

def com_RU3():
    ru_3=radio_7.get()
    if ru_3==1:
        a=1
    elif ru_3==2:
        a=2
    elif ru_3==3 or ru_3==4:
        a=3 
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position du poignet.")        
    return(a) 

def com_RU3_Ajust():
    ru_3_Ajust1=radio_8.get() 
    if  ru_3_Ajust1==True:
        b=1
    else:
        b=0
    return(b)    

def SE_3():
    a=com_RU3()
    b=com_RU3_Ajust()
    c=a+b
    return(c)

def SE_4():
    ru_4=radio_9.get() 
    if  ru_4==1:
        a=1
    elif ru_4==2: 
        a=2  
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la torsion du Poignet.")    
    return(a)       

def SE_5():
    a=SE_1()
    b=SE_2()
    c=SE_3()
    d=SE_4()
    filename_RULA_1='./fenetre1/RULA/TABLE_A_RULA.csv'
    data_1_RULA=[]
    with open(filename_RULA_1) as csvfile:
        csvreader=csv.reader(csvfile,delimiter=';')
        for i_RULA in csvreader:
            data_1_RULA.append(list(map(int,i_RULA)))
    Etape_5_RULA=TABLE_A_RULA(a,b,c,d,data_1_RULA)
    return(Etape_5_RULA)

def SE_7():
    ru_7=radio_10.get() 
    if ru_7==1:
        a=0
    elif ru_7==2:
        a=1
    elif ru_7==3:
        a=2
    elif ru_7==4:
        a=3   
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi \n le score d'effort et de charge de la partie superieur du corps.")     
    return(a)    

def SE_6():
    ru_6=radio_11.get() 
    if ru_6==True:
        b=1
    else:
        b=0                    
    return(b) 

def SE_8():
    c=SE_5()+SE_6()+SE_7()
    return(c)
 
def com_RU9():
    ru_9=radio_12.get()
    if ru_9==1:
        a=1
    elif ru_9==2:
        a=2
    elif ru_9==3:
        a=3
    elif ru_9==4:
        a=4    
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position de la nuque.")        
    return(a)       

def com_RU9_Ajust():
    ru_9_Ajust1=radio_13.get()
    ru_9_Ajust2=radio_14.get()
    if (ru_9_Ajust1==False and ru_9_Ajust2==False ):
        b=0
    elif (ru_9_Ajust1==True and ru_9_Ajust2==False) or (ru_9_Ajust1==False and ru_9_Ajust2==True):
        b=1
    else:
        b=2       
    return(b)   

def SE_9():
    a=com_RU9()+com_RU9_Ajust()
    return(a)


def com_RU10():
    ru_10=radio_15.get()
    if ru_10==1:
        a=1
    elif ru_10==2:
        a=2
    elif ru_10==3:
        a=3
    elif ru_10==4:
        a=4  
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position du tronc.") 
    return(a)                

           
def com_RU10_Ajust():
    ru_10_Ajust1=radio_16.get()
    ru_10_Ajust2=radio_17.get()
    if (ru_10_Ajust1==False and ru_10_Ajust2==False ):
        b=0
    elif (ru_10_Ajust1==True and ru_10_Ajust2==False) or (ru_10_Ajust1==False and ru_10_Ajust2==True):
        b=1
    else:
        b=2      
    return(b)
    


def SE_10():
    a=com_RU10()+com_RU10_Ajust()
    return(a)

def SE_11():
    ru_11=radio_18.get()
    if ru_11==1:
        a=2
    elif ru_11==2:
        a=1 
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position des jambes.")     
    return(a)        

def SE_12():
    a=SE_9()
    b=SE_10()
    c=SE_11()
    filename_RULA_2='./fenetre1/RULA/TABLE_B_RULA.csv'
    data_2_RULA=[]
    with open(filename_RULA_2) as csvfile:
        csvreader=csv.reader(csvfile,delimiter=';')
        for j_RULA in csvreader:
            data_2_RULA.append(list(map(int,j_RULA)))
    Etape_12_RULA=TABLE_B_RULA(a,b,c,data_2_RULA)
    return(Etape_12_RULA)
       

def SE_14():
    ru_14=radio_19.get() 
    if ru_14==1:
        a=0
    elif ru_14==2:
        a=1
    elif ru_14==3:
        a=2
    elif ru_14==4:
        a=3  
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi \n le score d'effort et de charge de la partie inferieur du corps.")          
    return(a)    

def SE_13():
    ru_13=radio_20.get() 
    if ru_13==True:
        b=1
    else:
        b=0 
    return(b) 

def SE_15():
    c=SE_12()+SE_13()+SE_14()
    return(c)

def SE_16():
    a=SE_8()
    b=SE_15()
    filename_RULA_3='./fenetre1/RULA/TABLE_C_RULA.csv'
    data_3_RULA=[]
    with open(filename_RULA_3) as csvfile:
        csvreader=csv.reader(csvfile,delimiter=';')
        for k_RULA in csvreader:
            data_3_RULA.append(list(map(int,k_RULA)))
    Score_final_RULA=TABLE_C_RULA(a,b,data_3_RULA)
    return(Score_final_RULA)

def quitter():
    window.destroy()
    

def precedent():
    window.destroy()
    subprocess.call("python ./fenetre1/fenetre_1.py",shell=True)
    
def check():
    Score_final_RULA=SE_16()
    if ((1<=Score_final_RULA) and (Score_final_RULA<=2)):
        messagebox.showinfo("Resultat", "Score final RULA = {0} \n Risque n\xe9gligeable, pas d'action n\xe9cessaire.".format(Score_final_RULA))          
    elif ((3<=Score_final_RULA) and (Score_final_RULA<=4)):
        messagebox.showinfo("Resultat", "Score final RULA = {0} \n Risque faible, un changement peur etre n\xe9cessaire.".format(Score_final_RULA))          
    elif ((5<=Score_final_RULA) and (Score_final_RULA<=6)):
        messagebox.showinfo("Resultat", "Score final RULA = {0} \n Risque moyen , a am\xe9liorer bientot.".format(Score_final_RULA)) 
    elif (Score_final_RULA>6):
        messagebox.showinfo("Resultat", "Score final RULA = {0} \n Risque fort, a am\xe9liorer maintenant.".format(Score_final_RULA))
    else:
        messagebox.showinfo("Resultat", "Le score final ne peut pas etre inferieur a 1")

def press(event):
    a=event.keysym
    if a=="Return":
        check()     

path = './fenetre1/RULA/Homme.PNG'
img = cv2.imread(path)
pointslist = []

def mousePoints(event, x,y,flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointslist)
        if size != 0 and size %3 != 0:
            cv2.arrowedLine(img, tuple(pointslist[round((size-1)/3)*3]),(x, y), (0,0,255), 2)
        cv2.circle(img, (x, y),2,(0,0,255),cv2.FILLED)
        pointslist.append([x, y])
        print(pointslist)

def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])


def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    m1=gradient(pt1, pt2)
    m2=gradient(pt1,pt3)
    angR =math.atan((m2-m1)/(1+(m2*m1)))
    angD= round (math.degrees(angR))
    if angD<0:
        angD=abs(angD)
    elif angD>=0:
        angD=180-angD
    cv2. putText(img, str(angD), (pt1[0]-40,pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,1.5, (0,0,255), 2)


def angle_fn():
    global pointslist
    global img
    window.filename=filedialog.askopenfilename(initialdir="/gui/images", title="SelectAFile", filetypes=(("png files", "*.png"),("all files", "*.*")))
    path =window.filename
    print(path)
    if path=="":
        cv2.destroyWindow('Mesure des angles')
    else:    
        img = cv2.imread(path)
    while True:
        if len(pointslist) % 3 == 0 and len(pointslist) !=0:
            getAngle(pointslist)
        cv2.imshow('Mesure des angles', img)
        cv2.setMouseCallback('Mesure des angles', mousePoints)
        if cv2.waitKey(1) & 0XFF == ord('e'):
            pointslist = []
            img = cv2.imread (path)
        if cv2.waitKey(1) & 0XFF == ord('E'):
            pointslist = []
            img = cv2.imread (path)    
        if cv2.waitKey(1)&0xff==ord('q'):
            pointslist = []
            cv2.destroyWindow('Mesure des angles')
            break
        if cv2.waitKey(1)&0xff==ord('Q'):
            pointslist = []
            cv2.destroyWindow('Mesure des angles')
            break

     
#A-Analyse du bras et du du poignet
   #Etape 1 : position de l'epaule

label_1=Label(second_frame,text="Score de la position de l'\xe9paule :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_1.pack()
label_1.place(relx=0.5,y=40,anchor=CENTER)


telechargementRU1_1=PhotoImage(file="./fenetre1/RULA/rula/RU1_1.png")
RU1_1=Radiobutton(second_frame, image=telechargementRU1_1,fg="blue",var=radio_1,value=1,command=com_RU1,bg="white",activebackground="white")
RU1_1.pack(pady=8)
RU1_1.place(x=100,y=90)


telechargementRU1_2=PhotoImage(file="./fenetre1/RULA/rula/RU1_2.png")
RU1_2=Radiobutton(second_frame, image=telechargementRU1_2,fg="blue",var=radio_1,value=2,command=com_RU1,bg="white",activebackground="white")
RU1_2.pack(pady=8)
RU1_2.place(x=330,y=90)

telechargementRU1_3=PhotoImage(file="./fenetre1/RULA/rula/RU1_3.png")
RU1_3=Radiobutton(second_frame, image=telechargementRU1_3,fg="blue",var=radio_1,value=3,command=com_RU1,bg="white",activebackground="white")
RU1_3.pack(pady=8)
RU1_3.place(x=580,y=90)

telechargementRU1_4=PhotoImage(file="./fenetre1/RULA/rula/RU1_4.png")
RU1_4=Radiobutton(second_frame, image=telechargementRU1_4,fg="blue",var=radio_1,value=4,command=com_RU1,bg="white",activebackground="white")
RU1_4.pack(pady=8)
RU1_4.place(x=200,y=310)

telechargementRU1_5=PhotoImage(file="./fenetre1/RULA/rula/RU1_5.png")
RU1_5=Radiobutton(second_frame, image=telechargementRU1_5,fg="blue",var=radio_1,value=5,command=com_RU1,bg="white",activebackground="white")
RU1_5.pack(pady=8)
RU1_5.place(x=480,y=310)

label_2=Label(second_frame,text="Score de l'ajustement de la position de l'\xe9paule :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_2.pack()
label_2.place(relx=0.5,anchor=CENTER,y=560)


telechargementRU_Ajust1_1=PhotoImage(file="./fenetre1/RULA/rula/Ru_Ajus1_1.png")
RU_Ajust1_1=Checkbutton(second_frame, image=telechargementRU_Ajust1_1,fg="blue",var=radio_2,command=com_RU1_Ajust,bg="white",activebackground="white")
RU_Ajust1_1.pack(pady=8)
RU_Ajust1_1.place(x=80,y=610)

telechargementRU_Ajust1_2=PhotoImage(file="./fenetre1/RULA/rula/Ru_Ajus1_2.png")
RU_Ajust1_2=Checkbutton(second_frame, image=telechargementRU_Ajust1_2,fg="blue",var=radio_3,command=com_RU1_Ajust,bg="white",activebackground="white")
RU_Ajust1_2.pack(pady=8)
RU_Ajust1_2.place(x=330,y=610)

telechargementRU_Ajust1_3=PhotoImage(file="./fenetre1/RULA/rula/Ru_Ajus1_3.png")
RU_Ajust1_3=Checkbutton(second_frame, image=telechargementRU_Ajust1_3,fg="blue",var=radio_4,command=com_RU1_Ajust,bg="white",activebackground="white")
RU_Ajust1_3.pack(pady=8)
RU_Ajust1_3.place(x=580,y=610)

   #Etape 2 : position du coude

label_3=Label(second_frame,text="Score de la position du coude :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_3.pack()
label_3.place(relx=0.5,anchor=CENTER,y=860)

telechargementRU2_1=PhotoImage(file="./fenetre1/RULA/rula/RU2_1.png")
RU2_1=Radiobutton(second_frame, image=telechargementRU2_1,fg="blue",var=radio_5,value=1,command=com_RU2,bg="white",activebackground="white")
RU2_1.pack(pady=8)
RU2_1.place(x=80,y=910)


telechargementRU2_2=PhotoImage(file="./fenetre1/RULA/rula/RU2_2.png")
RU2_2=Radiobutton(second_frame, image=telechargementRU2_2,fg="blue",var=radio_5,value=2,command=com_RU2,bg="white",activebackground="white")
RU2_2.pack(pady=8)
RU2_2.place(x=330,y=910)

telechargementRU2_3=PhotoImage(file="./fenetre1/RULA/rula/RU2_3.png")
RU2_3=Radiobutton(second_frame, image=telechargementRU2_3,fg="blue",var=radio_5,value=3,command=com_RU2,bg="white",activebackground="white")
RU2_3.pack(pady=8)
RU2_3.place(x=580,y=910)


label_4=Label(second_frame,text="Score de l'ajustement de la position du coude :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_4.pack()
label_4.place(relx=0.5,anchor=CENTER,y=1160)


telechargementRU_Ajust2_1=PhotoImage(file="./fenetre1/RULA/rula/Ru_Ajus2_1.png")
RU_Ajust2_1=Checkbutton(second_frame, image=telechargementRU_Ajust2_1,fg="blue",var=radio_6,command=com_RU2_Ajust,bg="white",activebackground="white")
RU_Ajust2_1.pack(pady=8)
RU_Ajust2_1.place(x=330,y=1210)

   #Etape 3 : position du poignet

label_5=Label(second_frame,text="Score de la position du poignet :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_5.pack()
label_5.place(relx=0.5,anchor=CENTER,y=1460)


telechargementRU3_1=PhotoImage(file="./fenetre1/RULA/rula/RU3_1.png")
RU3_1=Radiobutton(second_frame, image=telechargementRU3_1,fg="blue",var=radio_7,value=1,command=com_RU3,bg="white",activebackground="white")
RU3_1.pack(pady=8)
RU3_1.place(x=20,y=1510)


telechargementRU3_2=PhotoImage(file="./fenetre1/RULA/rula/RU3_2.png")
RU3_2=Radiobutton(second_frame, image=telechargementRU3_2,fg="blue",var=radio_7,value=2,command=com_RU3,bg="white",activebackground="white")
RU3_2.pack(pady=8)
RU3_2.place(x=220,y=1510)

telechargementRU3_3=PhotoImage(file="./fenetre1/RULA/rula/RU3_3.png")
RU3_3=Radiobutton(second_frame, image=telechargementRU3_3,fg="blue",var=radio_7,value=3,command=com_RU3,bg="white",activebackground="white")
RU3_3.pack(pady=8)
RU3_3.place(x=420,y=1510)

telechargementRU3_4=PhotoImage(file="./fenetre1/RULA/rula/RU3_4.png")
RU3_4=Radiobutton(second_frame, image=telechargementRU3_4,fg="blue",var=radio_7,value=4,command=com_RU3,bg="white",activebackground="white")
RU3_4.pack(pady=8)
RU3_4.place(x=620,y=1510)   

label_6=Label(second_frame,text="Score de l'ajustement de la position du poignet :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_6.pack()
label_6.place(relx=0.5,anchor=CENTER,y=1760)



telechargementRU_Ajust3_1=PhotoImage(file="./fenetre1/RULA/rula/Ru_Ajus3.png")
RU_Ajust3_1=Checkbutton(second_frame, image=telechargementRU_Ajust3_1,fg="blue",var=radio_8,bg="white",activebackground="white")
RU_Ajust3_1.pack(pady=8)
RU_Ajust3_1.place(x=330,y=1810)

   #Etape 4 : Torsion du poignet


label_7=Label(second_frame,text="Score de la torsion du poignet :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_7.pack()
label_7.place(relx=0.5,anchor=CENTER,y=2060)


telechargementRU4_1=PhotoImage(file="./fenetre1/RULA/rula/Ru4_1.png")
RU4_1=Radiobutton(second_frame, image=telechargementRU4_1,fg="blue",var=radio_9,value=1,command=SE_4,bg="white",activebackground="white")
RU4_1.pack(pady=8)
RU4_1.place(x=200,y=2110)


telechargementRU4_2=PhotoImage(file="./fenetre1/RULA/rula/Ru4_2.png")
RU4_2=Radiobutton(second_frame, image=telechargementRU4_2,fg="blue",var=radio_9,value=2,command=SE_4,bg="white",activebackground="white")
RU4_2.pack(pady=8)
RU4_2.place(x=480,y=2110)

   #Etape 6 et 7 : activite musculaire et score d'effort et de charge


label_8=Label(second_frame,text="Sélectionnez la force et la charge de la partie superieur du corps qui reflètent le mieux la situation de travail :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_8.pack()
label_8.place(relx=0.5,anchor=CENTER,y=2350)


RU7_1=Radiobutton(second_frame, text="La charge est inférieure à 2kg par intermittence",fg="black",var=radio_10,value=1,bg="white",activebackground="white",command=SE_7)
RU7_1.pack(pady=8)
RU7_1.place(x=40,y=2410)


RU7_2=Radiobutton(second_frame, text="La charge est entre 2kg et 10kg par intermittence",fg="black",var=radio_10,value=2,bg="white",activebackground="white",command=SE_7)
RU7_2.pack(pady=8)
RU7_2.place(x=40,y=2470)


RU7_3=Radiobutton(second_frame, text="La charge est entre 2kg et 10 kg avec une posture statique ou répétitive",fg="black",var=radio_10,value=3,bg="white",activebackground="white",command=SE_7)
RU7_3.pack(pady=8)
RU7_3.place(x=420,y=2410)


RU7_4=Radiobutton(second_frame, text="La charge est supérieure à 10kg avec répétitivité ou chocs",fg="black",var=radio_10,value=4,bg="white",activebackground="white",command=SE_7)
RU7_4.pack(pady=8)
RU7_4.place(x=420,y=2470)  

label_9=Label(second_frame,text="Cochez cette case si elle reflète votre utilisation musculaire :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_9.pack()
label_9.place(relx=0.5,anchor=CENTER,y=2540)

RU_6=Checkbutton(second_frame, text="La posture est maintenue statique pendant plus de 10 minutes ou répétée plus de 4 fois par minute.",fg="black",var=radio_11,bg="white",activebackground="white",command=SE_6)
RU_6.pack(pady=8)
RU_6.place(x=230,y=2600)

   #Etape 9 : position de la nuque


label_10=Label(second_frame,text="Score de la position de la nuque :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_10.pack()
label_10.place(relx=0.5,anchor=CENTER,y=2700)


telechargementRU9_1=PhotoImage(file="./fenetre1/RULA/rula/RU9_1.png")
RU9_1=Radiobutton(second_frame, image=telechargementRU9_1,fg="blue",var=radio_12,value=1,bg="white",activebackground="white",command=com_RU9)
RU9_1.pack(pady=8)
RU9_1.place(x=20,y=2750)


telechargementRU9_2=PhotoImage(file="./fenetre1/RULA/rula/RU9_2.png")
RU9_2=Radiobutton(second_frame, image=telechargementRU9_2,fg="blue",var=radio_12,value=2,bg="white",activebackground="white",command=com_RU9)
RU9_2.pack(pady=8)
RU9_2.place(x=220,y=2750)

telechargementRU9_3=PhotoImage(file="./fenetre1/RULA/rula/RU9_3.png")
RU9_3=Radiobutton(second_frame, image=telechargementRU9_3,fg="blue",var=radio_12,value=3,bg="white",activebackground="white",command=com_RU9)
RU9_3.pack(pady=8)
RU9_3.place(x=420,y=2750)

telechargementRU9_4=PhotoImage(file="./fenetre1/RULA/rula/RU9_4.png")
RU9_4=Radiobutton(second_frame, image=telechargementRU9_4,fg="blue",var=radio_12,value=4,bg="white",activebackground="white",command=com_RU9)
RU9_4.pack(pady=8)
RU9_4.place(x=620,y=2750)   

label_11=Label(second_frame,text="Score de l'ajustement de la position de la nuque :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_11.pack()
label_11.place(relx=0.5,anchor=CENTER,y=3000)

telechargementRU_Ajust9_1=PhotoImage(file="./fenetre1/RULA/rula/Ru_Ajus9_1.png")
RU_Ajust9_1=Checkbutton(second_frame,image=telechargementRU_Ajust9_1 ,fg="blue",var=radio_13,bg="white",activebackground="white",command=com_RU9_Ajust)
RU_Ajust9_1.pack(pady=8)
RU_Ajust9_1.place(x=200,y=3050)

telechargementRU_Ajust9_2=PhotoImage(file="./fenetre1/RULA/rula/Ru_Ajus9_2.png")
RU_Ajust9_2=Checkbutton(second_frame,image=telechargementRU_Ajust9_2,fg="blue",var=radio_14,bg="white",activebackground="white",command=com_RU9_Ajust)
RU_Ajust9_2.pack(pady=8)
RU_Ajust9_2.place(x=480,y=3050)


   #Etape 10 : position du tronc


label_12=Label(second_frame,text="Score de la position du tronc :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_12.pack()
label_12.place(relx=0.5,anchor=CENTER,y=3300)



telechargementRU10_1=PhotoImage(file="./fenetre1/RULA/rula/Ru10_1.png")
RU10_1=Radiobutton(second_frame, image=telechargementRU10_1,fg="blue",var=radio_15,value=1,bg="white",activebackground="white",command=com_RU10)
RU10_1.pack(pady=8)
RU10_1.place(x=20,y=3350)


telechargementRU10_2=PhotoImage(file="./fenetre1/RULA/rula/Ru10_2.png")
RU10_2=Radiobutton(second_frame, image=telechargementRU10_2,fg="blue",var=radio_15,value=2,bg="white",activebackground="white",command=com_RU10)
RU10_2.pack(pady=8)
RU10_2.place(x=220,y=3350)

telechargementRU10_3=PhotoImage(file="./fenetre1/RULA/rula/Ru10_3.png")
RU10_3=Radiobutton(second_frame, image=telechargementRU10_3,fg="blue",var=radio_15,value=3,bg="white",activebackground="white",command=com_RU10)
RU10_3.pack(pady=8)
RU10_3.place(x=420,y=3350)

telechargementRU10_4=PhotoImage(file="./fenetre1/RULA/rula/Ru10_4.png")
RU10_4=Radiobutton(second_frame, image=telechargementRU10_4,fg="blue",var=radio_15,value=4,bg="white",activebackground="white",command=com_RU10)
RU10_4.pack(pady=8)
RU10_4.place(x=620,y=3350)  

label_13=Label(second_frame,text="Score de l'ajustement de la position du tronc :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_13.pack()
label_13.place(relx=0.5,anchor=CENTER,y=3600)

telechargementRU_Ajust10_1=PhotoImage(file="./fenetre1/RULA/rula/Ru_Ajus10_1.png")
RU_Ajust10_1=Checkbutton(second_frame,image=telechargementRU_Ajust10_1 ,fg="blue",var=radio_16,bg="white",activebackground="white",command=com_RU10_Ajust)
RU_Ajust10_1.pack(pady=8)
RU_Ajust10_1.place(x=200,y=3650)

telechargementRU_Ajust10_2=PhotoImage(file="./fenetre1/RULA/rula/RuAjus10_2.png")
RU_Ajust10_2=Checkbutton(second_frame,image=telechargementRU_Ajust10_2,fg="blue",var=radio_17,bg="white",activebackground="white",command=com_RU10_Ajust)
RU_Ajust10_2.pack(pady=8)
RU_Ajust10_2.place(x=480,y=3650)


   #Etape 11 : position des jambes


label_14=Label(second_frame,text="Score de la position des jambes :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_14.pack()
label_14.place(relx=0.5,anchor=CENTER,y=3900)


telechargementRU11_1=PhotoImage(file="./fenetre1/RULA/rula/Ru11_1.png")
RU11_1=Radiobutton(second_frame, image=telechargementRU11_1,fg="blue",var=radio_18,value=1,bg="white",activebackground="white",command=SE_11)
RU11_1.pack(pady=8)
RU11_1.place(x=200,y=3950)


telechargementRU11_2=PhotoImage(file="./fenetre1/RULA/rula/Ru11_2.png")
RU11_2=Radiobutton(second_frame, image=telechargementRU11_2,fg="blue",var=radio_18,value=2,bg="white",activebackground="white",command=SE_11)
RU11_2.pack(pady=8)
RU11_2.place(x=480,y=3950)

   #Etape 13 et 14 : activite musculaire et score d'effort et de charge


label_15=Label(second_frame,text="Sélectionnez la force et la charge de la inferieur du corps qui reflètent le mieux la situation de travail :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_15.pack()
label_15.place(relx=0.5,anchor=CENTER,y=4190)


RU14_1=Radiobutton(second_frame, text="La charge est inférieure à 2kg par intermittence",fg="black",var=radio_19,value=1,bg="white",activebackground="white",command=SE_14)
RU14_1.pack(pady=8)
RU14_1.place(x=40,y=4250)


RU14_2=Radiobutton(second_frame, text="La charge est entre 2kg et 10kg par intermittence",fg="black",var=radio_19,value=2,bg="white",activebackground="white",command=SE_14)
RU14_2.pack(pady=8)
RU14_2.place(x=40,y=4310)


RU14_3=Radiobutton(second_frame, text="La charge est entre 2kg et 10 kg avec une posture statique ou répétitive",fg="black",var=radio_19,value=3,bg="white",activebackground="white",command=SE_14)
RU14_3.pack(pady=8)
RU14_3.place(x=420,y=4250)


RU14_4=Radiobutton(second_frame, text="La charge est supérieure à 10kg avec répétitivité ou chocs",fg="black",var=radio_19,value=4,bg="white",activebackground="white",command=SE_14)
RU14_4.pack(pady=8)
RU14_4.place(x=420,y=4310)  

label_16=Label(second_frame,text="Cochez cette case si elle reflète votre utilisation musculaire :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_16.pack()
label_16.place(x=180,y=4380)

RU_13=Checkbutton(second_frame, text="La posture est maintenue statique pendant plus de 10 minutes ou répétée plus de 4 fois par minute.",fg="black",var=radio_20,bg="white",activebackground="white",command=SE_13)
RU_13.pack(pady=8)
RU_13.place(x=230,y=4440)

   #buttons

telechargement_check=PhotoImage(file="./fenetre1/RULA/check.png")
button_1=Button(second_frame,image=telechargement_check,font=("Times New Roman",17),fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=check)
button_1.pack()
button_1.place(relx=0.5,y=4530,anchor=CENTER)
button_1.bind_all('<Key>',press)

telechargement_precedent1=PhotoImage(file="./fenetre1/RULA/precedent.png")
button_2=Button(second_frame,image=telechargement_precedent1,font=("Times New Roman",17),fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=precedent)
button_2.pack()
button_2.place(x=100,y=4500)

telechargement_precedent2=PhotoImage(file="./fenetre1/RULA/precedent.png")
button_21=Button(second_frame,image=telechargement_precedent2,font=("Times New Roman",17),fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=precedent)
button_21.pack()
button_21.place(x=20,y=30)

telechargement_quitter=PhotoImage(file="./fenetre1/RULA/quitter.png")
button_3=Button(second_frame,image=telechargement_quitter,font=("Times New Roman",17),fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=quitter)
button_3.pack()
button_3.place(x=749,y=4500)

telechargement_angle=PhotoImage(file="./fenetre1/RULA/angle.png")
button_4=Button(second_frame,image=telechargement_angle,fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=angle_fn)
button_4.pack()
button_4.place(x=800,y=30)

second_frame.configure(height=4600)
window.mainloop()
