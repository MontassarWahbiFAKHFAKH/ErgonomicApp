from ast import Lambda
from tkinter import *
from tkinter import messagebox
import tkinter as ttk
import os
import csv
import sys
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import math
import subprocess

window = Tk()
window.title("REBA (Rapid Entire Body Assessment)")
radio_1=IntVar()
radio_2=BooleanVar()
radio_3=BooleanVar()
radio_4=IntVar()
radio_5=BooleanVar()
radio_6=BooleanVar()
radio_7=IntVar()
radio_8=BooleanVar()
radio_9=BooleanVar()
radio_10=IntVar()
radio_11=BooleanVar()
radio_12=IntVar()
radio_13=BooleanVar()
radio_14=BooleanVar()
radio_15=BooleanVar()
radio_16=IntVar()
radio_17=IntVar()
radio_18=BooleanVar()
radio_19=BooleanVar()
radio_20=IntVar()
radio_21=BooleanVar()
radio_22=BooleanVar()
radio_23=BooleanVar()

alto=520
ancho=900
anchoalto="900x520"
window.geometry(anchoalto)
window.resizable(0,0)
window.iconbitmap("./fenetre1/REBA/icon.ico")
window.config(bg="white")
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

def TABLE_A_REBA(Etape_2_REBA,Etape_1_REBA,Etape_3_REBA,data_1_REBA):
    Ligne1_REBA=Etape_2_REBA+1
    Resultat1_REBA=data_1_REBA[Ligne1_REBA][Etape_3_REBA+(Etape_1_REBA*2)+((Etape_1_REBA-2)*2)]
    return(Resultat1_REBA)

def TABLE_B_REBA(Etape_7_REBA,Etape_8_REBA,Etape_9_REBA,data_2_REBA):
    Ligne2_REBA=Etape_7_REBA+1
    if Etape_8_REBA==1:
        Resultat2_REBA=data_2_REBA[Ligne2_REBA][Etape_9_REBA]
    elif Etape_8_REBA==2:
        Resultat2_REBA=data_2_REBA[Ligne2_REBA][Etape_9_REBA+3]
    else:
        pass    
    return(Resultat2_REBA)

def TABLE_C_REBA(Etape_6_REBA,Etape_12_REBA,data_3_REBA):
    Ligne3_REBA=Etape_6_REBA
    if Etape_6_REBA>12:
        Ligne3_REBA=12
    Colone_REBA=Etape_12_REBA
    if Etape_12_REBA>12:
        Colone_REBA=12
    Resultat3_REBA=data_3_REBA[Ligne3_REBA][Colone_REBA]
    return(Resultat3_REBA)

def com_RE1():
    re_1=radio_1.get()
    if re_1==1:
        a=1
    elif re_1==2 or re_1==3:
        a=2 
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position de la nuque.")                   
    return(a)

def com_RE1_Ajust():
    re_1_Ajust1=radio_2.get()
    re_1_Ajust2=radio_3.get()
    if (re_1_Ajust1==True and re_1_Ajust2==False )or(re_1_Ajust1==False and re_1_Ajust2==True ) :
        b=1
    elif (re_1_Ajust1==True and re_1_Ajust2==True ):
        b=2    
    else: 
        b=0          
    return(b)    

def SE_1():
    a=com_RE1()
    b=com_RE1_Ajust()
    if (a==2 and b==2):
        messagebox.showerror("Erreur", "La somme du score de la position de la nuque avec le score de l'ajustement de la position de la nuque ne peut pas etre egal a 4.") 
    else:
        c=a+b   
    return(c)  

def com_RE2():
    re_2=radio_4.get()
    if re_2==2 or re_2==3:
        a=2
    elif re_2==1:
        a=1
    elif re_2==4:
        a=3
    elif re_2==5:
        a=4     
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position du tronc.")            
    return(a)

def com_RE2_Ajust():
     re_2_Ajust1=radio_5.get() 
     re_2_Ajust2=radio_6.get()  
     b=0  
     if (re_2_Ajust1==True and re_2_Ajust2==False )or(re_2_Ajust1==False and re_2_Ajust2==True ):
         b=1
     elif (re_2_Ajust1==False and re_2_Ajust2==False):
         b=0
     else:
         b=2       
     return(b)     

def SE_2():
    a=com_RE2()
    b=com_RE2_Ajust()
    if (a==4 and b==2):
        messagebox.showerror("Erreur", "La somme du score de la position du tronc avec le score de l'ajustement de la position du tronc ne peut pas etre egal a 6.") 
    else:
        c=a+b
    return(c)   

def com_RE3():
    re_3=radio_7.get()
    if re_3==1 :
        a=1
    elif re_3==2:
        a=2
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position des jambes.")       

    return(a) 
    

def com_RE3_Ajust():
    re_3_Ajust1=radio_8.get() 
    re_3_Ajust2=radio_9.get()
    
    if (re_3_Ajust1==True and re_3_Ajust2==False ):
         b=1
    elif (re_3_Ajust1==False and re_3_Ajust2==True):
         b=2
    elif (re_3_Ajust1==False and re_3_Ajust2==False):
        b=0     
    else:
        b=3      
    return(b)    

def SE_3():
    a=com_RE3()
    b=com_RE3_Ajust()
    if (a==2 and b==3):
        messagebox.showerror("Erreur", "La somme du score de la position des jambes avec le score de l'ajustement de la position des jambes ne peut pas etre egal a 5.") 
    else:
        c=a+b
    return(c) 
     

def SE_4():
    a=SE_1()
    b=SE_2()
    c=SE_3()
    filename_REBA_1='./fenetre1/REBA/TABLE_A_REBA.csv'
    data_1_REBA=[]
    with open(filename_REBA_1) as csvfile:
        csvreader=csv.reader(csvfile,delimiter=';')
        for i_RULA in csvreader:
            data_1_REBA.append(list(map(int,i_RULA)))
    Etape_4_REBA=TABLE_A_REBA(b,a,c,data_1_REBA) 
    print(Etape_4_REBA)
    return(Etape_4_REBA)
   
    
def SE_5():
    ru_5=radio_10.get()
    if ru_5==1:
        E=0
    elif ru_5==2:
        E=1
    elif ru_5==3:
        E=3
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score d'effort et de charge.")         
    return(E) 

def SE_6():
    re_5_Ajust1=radio_11.get() 
    if (re_5_Ajust1==True):
        b=1 
    else:
        b=0  
    return(b)    


def Somme_SE_4_5_6():
    a=SE_4()+SE_5()+SE_6()
    return(a)


def com_RE7():
    re_7=radio_12.get()
    if re_7==2 or re_7==3:
        a=2
    elif re_7==1:
        a=1
    elif re_7==4:
        a=3
    elif re_7==5:
        a=4   
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position du bras.")          
    return(a)

def com_RE7_Ajust():
     re_7_Ajust1=radio_13.get() 
     re_7_Ajust2=radio_14.get()  
     re_7_Ajust3=radio_15.get()
     if (re_7_Ajust1==True and re_7_Ajust2==False and re_7_Ajust3== False)or(re_7_Ajust1==False and re_7_Ajust2==True and re_7_Ajust3== False )or(re_7_Ajust1==True and re_7_Ajust2==True and re_7_Ajust3== True ):
         b=1
     elif (re_7_Ajust1==False and re_7_Ajust2==False and re_7_Ajust3== False)or(re_7_Ajust1==True and re_7_Ajust2==False and re_7_Ajust3== True ) or(re_7_Ajust1==False and re_7_Ajust2==True and re_7_Ajust3== True ):
         b=0
     elif (re_7_Ajust1==False and re_7_Ajust2==False and re_7_Ajust3== True):
         b=-1
     else:
         b=2         
     return(b)     

def SE_7():
    c=com_RE7()+com_RE7_Ajust()
    return(c)

def SE_8():
    re_8=radio_16.get()
    if re_8==1:
        a=1
    elif re_8==2 or re_8==3:
        a=2  
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position de l'avant bras.")               
    return(a)

def com_RE9():
    re_9=radio_17.get()
    if re_9==1:
        a=1
    elif re_9==2 or re_9==3:
        a=2   
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la position du poignet.")               
    return(a)

def com_RE9_Ajust():
    re_9_Ajust1=radio_18.get()
    re_9_Ajust2=radio_19.get()
    if (re_9_Ajust1==True and re_9_Ajust2==False )or(re_9_Ajust1==False and re_9_Ajust2==True ) :
        b=1
    elif (re_9_Ajust1==True and re_9_Ajust2==True ):
        b=2
    else: 
        b=0  
            
    return(b)    

def SE_9():
    a=com_RE9()
    b=com_RE9_Ajust()
    if (a==2 and b==2):
        messagebox.showerror("Erreur", "La somme du score de la position du poignet avec le score de l'ajustement de la position du poignet ne peut pas etre egal a 4.") 
    else:
        c=a+b
    return(c) 
    
    
def SE_10():
    a=SE_7()
    b=SE_8()
    c=SE_9()
    filename_REBA_2='./fenetre1/REBA/TABLE_B_REBA.csv'
    data_2_REBA=[]
    with open(filename_REBA_2) as csvfile:
        csvreader=csv.reader(csvfile,delimiter=';')
        for j_REBA in csvreader:
            data_2_REBA.append(list(map(int,j_REBA)))
    Etape_10_REBA=TABLE_B_REBA(a,b,c,data_2_REBA)  
    return(Etape_10_REBA)
  

def SE_11():
    re_11=radio_20.get()
    if re_11==1:
        a=0
    elif re_11==2:
        a=1
    elif re_11==3:
        a=2
    elif re_11==4:
        a=3  
    else:
        messagebox.showerror("Erreur", "Il semble que vous n'avez pas choisi le score de la fascilité de la prise.")        
    return(a)  

def SE_12():
    a=SE_10()+SE_11()  
    return(a)  

def SE_13():
    a=Somme_SE_4_5_6()
    b=SE_12()
    filename_REBA_3='./fenetre1/REBA/TABLE_C_REBA.csv'
    data_3_REBA=[]
    with open(filename_REBA_3) as csvfile:
        csvreader=csv.reader(csvfile,delimiter=';')
        for k_REBA in csvreader:
            data_3_REBA.append(list(map(int,k_REBA)))
    Etape_13_REBA=TABLE_C_REBA(a,b,data_3_REBA)  
    return(Etape_13_REBA)   

def SE_14():
    re_14=radio_21.get()
    re_15=radio_22.get()
    re_16=radio_23.get()
    if (re_14==True and re_15==False and re_16==False) or (re_14==False and re_15==True and re_16==False) or (re_14==False and re_15==False and re_16==True):
        a=1
    elif (re_14==False and re_15==False and re_16==False):
        a=0    
    else:
        messagebox.showerror("Erreur", "Ce n'est pas possible d'avoir plusieurs choix pour le score d'activité.")    
    return(a)   
    
        
def score_final_reba():
    a=SE_13()+SE_14()   
    return(a)

def quitter():
    window.destroy()

def precedent():
    window.destroy()
    subprocess.call("python ./fenetre1/fenetre_1.py",shell=True)
    
def press(event):
    a=event.keysym
    if a=="Return":
        check()

def check():

    Score_final_REBA=score_final_reba()
    if Score_final_REBA==1:
        messagebox.showinfo("Resultat", "Score final REBA = {0} \n Risque n\xe9gligeable.".format(Score_final_REBA))
    elif Score_final_REBA>=2 and Score_final_REBA<=3:
        messagebox.showinfo("Resultat", "Score final REBA = {0} \n Risque faible.".format(Score_final_REBA))
    elif Score_final_REBA>=4 and Score_final_REBA<=7:
         messagebox.showinfo("Resultat", "Score final REBA = {0} \n Risque moyen.".format(Score_final_REBA))
    elif Score_final_REBA>=8 and Score_final_REBA<=10:
        messagebox.showinfo("Resultat", "Score final REBA = {0} \n Risque \xe9lev\xe9.".format(Score_final_REBA))
    elif Score_final_REBA>=11:
        messagebox.showinfo("Resultat", "Score final REBA = {0} \n Risque tres \xe9lev\xe9.".format(Score_final_REBA))
    else:
        messagebox.showinfo("Resultat", "Le score final ne peut pas etre inferieur a 1")



path = './fenetre1/REBA/Homme.PNG'
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
   #Etape 1 : position de la nuque

label_1=Label(second_frame,text="Score de la position de la nuque :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_1.pack()
label_1.place(relx=0.5,y=40,anchor=CENTER)

telechargementRE1_1=PhotoImage(file="./fenetre1/REBA/reba/re1_1.png")
RE1_1=Radiobutton(second_frame, image=telechargementRE1_1,fg="blue",var=radio_1,value=1,command=com_RE1,bg="white",activebackground="white")
RE1_1.pack(pady=8)
RE1_1.place(x=100,y=90)


telechargementRE1_2=PhotoImage(file="./fenetre1/REBA/reba/re1_2.png")
RE1_2=Radiobutton(second_frame, image=telechargementRE1_2,fg="blue",var=radio_1,value=2,command=com_RE1,bg="white",activebackground="white")
RE1_2.pack(pady=8)
RE1_2.place(x=330,y=90)

telechargementRE1_3=PhotoImage(file="./fenetre1/REBA/reba/re1_3.png")
RE1_3=Radiobutton(second_frame, image=telechargementRE1_3,fg="blue",var=radio_1,value=3,command=com_RE1,bg="white",activebackground="white")
RE1_3.pack(pady=8)
RE1_3.place(x=580,y=90)

label_2=Label(second_frame,text="Score de l'justement de la position de la nuque :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_2.pack()
label_2.place(relx=0.5,y=310,anchor=CENTER)

telechargementRE_Ajust1_1=PhotoImage(file="./fenetre1/REBA/reba/Re1_Ajus1_1.png")
RE_Ajust1_1=Checkbutton(second_frame, image=telechargementRE_Ajust1_1,fg="blue",var=radio_2,command=com_RE1_Ajust,bg="white",activebackground="white")
RE_Ajust1_1.pack(pady=8)
RE_Ajust1_1.place(x=200,y=360)

telechargementRE_Ajust1_2=PhotoImage(file="./fenetre1/REBA/reba/re1_Ajus1_2.png")
RE_Ajust1_2=Checkbutton(second_frame, image=telechargementRE_Ajust1_2,fg="blue",var=radio_3,command=com_RE1_Ajust,bg="white",activebackground="white")
RE_Ajust1_2.pack(pady=8)
RE_Ajust1_2.place(x=480,y=360)

   #Etape 2 : position du tronc

label_3=Label(second_frame,text="Score de la position du tronc :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_3.pack()
label_3.place(relx=0.5,y=580,anchor=CENTER)

telechargementRE2_1=PhotoImage(file="./fenetre1/REBA/reba/re2_1.png")
RE2_1=Radiobutton(second_frame, image=telechargementRE2_1,fg="blue",var=radio_4,value=1,command=com_RE2,bg="white",activebackground="white")
RE2_1.pack(pady=8)
RE2_1.place(x=80,y=630)

telechargementRE2_2=PhotoImage(file="./fenetre1/REBA/reba/re2_2.png")
RE2_2=Radiobutton(second_frame, image=telechargementRE2_2,fg="blue",var=radio_4,value=2,command=com_RE2,bg="white",activebackground="white")
RE2_2.pack(pady=8)
RE2_2.place(x=330,y=630)

telechargementRE2_3=PhotoImage(file="./fenetre1/REBA/reba/re2_3.png")
RE2_3=Radiobutton(second_frame, image=telechargementRE2_3,fg="blue",var=radio_4,value=3,command=com_RE2,bg="white",activebackground="white")
RE2_3.pack(pady=8)
RE2_3.place(x=580,y=630)

telechargementRE2_4=PhotoImage(file="./fenetre1/REBA/reba/re2_4.png")
RE2_4=Radiobutton(second_frame, image=telechargementRE2_4,fg="blue",var=radio_4,value=4,command=com_RE2,bg="white",activebackground="white")
RE2_4.pack(pady=8)
RE2_4.place(x=200,y=850)

telechargementRE2_5=PhotoImage(file="./fenetre1/REBA/reba/re2_5.png")
RE2_5=Radiobutton(second_frame, image=telechargementRE2_5,fg="blue",var=radio_4,value=5,command=com_RE2,bg="white",activebackground="white")
RE2_5.pack(pady=8)
RE2_5.place(x=480,y=850)

label_4=Label(second_frame,text="Score de l'ajustement de la position du tronc :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_4.pack()
label_4.place(relx=0.5,y=1070,anchor=CENTER)

telechargementRE_Ajust2_1=PhotoImage(file="./fenetre1/REBA/reba/re_Ajus2_1.PNG")
RE_Ajust2_1=Checkbutton(second_frame, image=telechargementRE_Ajust2_1,fg="blue",var=radio_5,command=com_RE2_Ajust,bg="white",activebackground="white")
RE_Ajust2_1.pack(pady=8)
RE_Ajust2_1.place(x=200,y=1120)

telechargementRE_Ajust2_2=PhotoImage(file="./fenetre1/REBA/reba/re_Ajus2_2.PNG")
RE_Ajust2_2=Checkbutton(second_frame, image=telechargementRE_Ajust2_2,fg="blue",var=radio_6,command=com_RE2_Ajust,bg="white",activebackground="white")
RE_Ajust2_2.pack(pady=8)
RE_Ajust2_2.place(x=480,y=1120)

   #Etape 3 : position des jambes

label_5=Label(second_frame,text="Score de la position des jambes :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_5.pack()
label_5.place(relx=0.5,y=1340,anchor=CENTER)


telechargementRE3_1=PhotoImage(file="./fenetre1/REBA/reba/re3_1.png")
RE3_1=Radiobutton(second_frame, image=telechargementRE3_1,fg="blue",var=radio_7,value=1,command=com_RE3,bg="white",activebackground="white")
RE3_1.pack(pady=8)
RE3_1.place(x=200,y=1390)

telechargementRE3_2=PhotoImage(file="./fenetre1/REBA/reba/re3_2.png")
RE3_2=Radiobutton(second_frame, image=telechargementRE3_2,fg="blue",var=radio_7,value=2,command=com_RE3,bg="white",activebackground="white")
RE3_2.pack(pady=8)
RE3_2.place(x=480,y=1390)

label_6=Label(second_frame,text="Score de l'ajustement de la position des jambes :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_6.pack()
label_6.place(x=280,y=1610)

telechargementRE_Ajust3_1=PhotoImage(file="./fenetre1/REBA/reba/re3_Ajus3_1.png")
RE_Ajust3_1=Checkbutton(second_frame, image=telechargementRE_Ajust3_1,fg="blue",var=radio_8,command=com_RE3_Ajust,bg="white",activebackground="white")
RE_Ajust3_1.pack(pady=8)
RE_Ajust3_1.place(x=200,y=1660)

telechargementRE_Ajust3_2=PhotoImage(file="./fenetre1/REBA/reba/re3_Ajus3_2.png")
RE_Ajust3_2=Checkbutton(second_frame, image=telechargementRE_Ajust3_2,fg="blue",var=radio_9,command=com_RE3_Ajust,bg="white",activebackground="white")
RE_Ajust3_2.pack(pady=8)
RE_Ajust3_2.place(x=480,y=1660)


   #Etape 5 : activite musculaire et score d'effort et de charge
label_7=Label(second_frame,text="Score d'effort et de charge :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_7.pack()
label_7.place(relx=0.5,y=1880,anchor=CENTER)

RE5_1=Radiobutton(second_frame, text="La charge est inférieure à 5kg ",fg="black",var=radio_10,value=1,command=SE_5,bg="white",activebackground="white")
RE5_1.pack(pady=8)
RE5_1.place(x=80,y=1930)


RE5_2=Radiobutton(second_frame, text="La charge est entre 5kg et 10kg ",fg="black",var=radio_10,value=2,command=SE_5,bg="white",activebackground="white")
RE5_2.pack(pady=8)
RE5_2.place(relx=0.5,y=1980,anchor=CENTER)


RE5_3=Radiobutton(second_frame, text="La charge est supérieure à 10 kg ",fg="black",var=radio_10,value=3,command=SE_5,bg="white",activebackground="white")
RE5_3.pack(pady=8)
RE5_3.place(x=630,y=1930)

#Etape 6 : score A

RE_Ajust5_1=Checkbutton(second_frame,  text="Si choc, changement de posture violent ou grande répététivité",fg="black",var=radio_11,command=SE_6,bg="white",activebackground="white")
RE_Ajust5_1.pack(pady=8)
RE_Ajust5_1.place(relx=0.5,y=2020,anchor=CENTER)

#Etape 7 : position du bras

label_8=Label(second_frame,text="Score de la position du bras :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_8.pack()
label_8.place(relx=0.5,y=2070,anchor=CENTER)

telechargementRE7_1=PhotoImage(file="./fenetre1/REBA/reba/re7_1.png")
RE7_1=Radiobutton(second_frame, image=telechargementRE7_1,fg="blue",var=radio_12,value=1,command=com_RE7,bg="white",activebackground="white")
RE7_1.pack(pady=8)
RE7_1.place(x=80,y=2120)

telechargementRE7_2=PhotoImage(file="./fenetre1/REBA/reba/re7_2.png")
RE7_2=Radiobutton(second_frame, image=telechargementRE7_2,fg="blue",var=radio_12,value=2,command=com_RE7,bg="white",activebackground="white")
RE7_2.pack(pady=8)
RE7_2.place(x=330,y=2120)

telechargementRE7_3=PhotoImage(file="./fenetre1/REBA/reba/re7_3.png")
RE7_3=Radiobutton(second_frame, image=telechargementRE7_3,fg="blue",var=radio_12,value=3,command=com_RE7,bg="white",activebackground="white")
RE7_3.pack(pady=8)
RE7_3.place(x=580,y=2120)

telechargementRE7_4=PhotoImage(file="./fenetre1/REBA/reba/re7_4.png")
RE7_4=Radiobutton(second_frame, image=telechargementRE7_4,fg="blue",var=radio_12,value=4,command=com_RE7,bg="white",activebackground="white")
RE7_4.pack(pady=8)
RE7_4.place(x=200,y=2340)

telechargementRE7_5=PhotoImage(file="./fenetre1/REBA/reba/re7_5.png")
RE7_5=Radiobutton(second_frame, image=telechargementRE7_5,fg="blue",var=radio_12,value=5,command=com_RE7,bg="white",activebackground="white")
RE7_5.pack(pady=8)
RE7_5.place(x=480,y=2340)

label_9=Label(second_frame,text="Score de l'ajustement de la position du bras :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_9.pack()
label_9.place(relx=0.5,y=2560,anchor=CENTER)

RE_Ajust7_1=Checkbutton(second_frame,text= "Epaule levé" ,fg="black",var=radio_13,command=com_RE7_Ajust,bg="white",activebackground="white")
RE_Ajust7_1.pack(pady=8)
RE_Ajust7_1.place(x=130,y=2600)

RE_Ajust7_2=Checkbutton(second_frame,text= "Bras en abduction",fg="black",var=radio_14,command=com_RE7_Ajust,bg="white",activebackground="white")
RE_Ajust7_2.pack(pady=8)
RE_Ajust7_2.place(relx=0.5,y=2610,anchor=CENTER)

RE_Ajust7_3=Checkbutton(second_frame,text= "Le bras est soutenu ou la personne est penchée" ,fg="black",var=radio_15,command=com_RE7_Ajust,bg="white",activebackground="white")
RE_Ajust7_3.pack(pady=8)
RE_Ajust7_3.place(x=580,y=2600)

#Etape 8 : position de l'avant bras

label_10=Label(second_frame,text="Score de la position de l'avant bras :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_10.pack()
label_10.place(relx=0.5,y=2660,anchor=CENTER)

telechargementRE8_1=PhotoImage(file="./fenetre1/REBA/reba/re8_1.png")
RE8_1=Radiobutton(second_frame, image=telechargementRE8_1,fg="blue",var=radio_16,value=1,command=SE_8,bg="white",activebackground="white")
RE8_1.pack(pady=8)
RE8_1.place(x=100,y=2710)


telechargementRE8_2=PhotoImage(file="./fenetre1/REBA/reba/re8_2.png")
RE8_2=Radiobutton(second_frame, image=telechargementRE8_2,fg="blue",var=radio_16,value=2,command=SE_8,bg="white",activebackground="white")
RE8_2.pack(pady=8)
RE8_2.place(x=330,y=2710)

telechargementRE8_3=PhotoImage(file="./fenetre1/REBA/reba/re8_3.png")
RE8_3=Radiobutton(second_frame, image=telechargementRE8_3,fg="blue",var=radio_16,value=3,command=SE_8,bg="white",activebackground="white")
RE8_3.pack(pady=8)
RE8_3.place(x=580,y=2710)

   #Etape 9 : position du poignet

label_11=Label(second_frame,text="Score de la position du poignet :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_11.pack()
label_11.place(relx=0.5,y=2930,anchor=CENTER)

telechargementRE9_1=PhotoImage(file="./fenetre1/REBA/reba/re9_1.png")
RE9_1=Radiobutton(second_frame, image=telechargementRE9_1,fg="blue",var=radio_17,value=1,command=com_RE9,bg="white",activebackground="white")
RE9_1.pack(pady=8)
RE9_1.place(x=100,y=2980)


telechargementRE9_2=PhotoImage(file="./fenetre1/REBA/reba/re9_2.png")
RE9_2=Radiobutton(second_frame, image=telechargementRE9_2,fg="blue",var=radio_17,value=2,command=com_RE9,bg="white",activebackground="white")
RE9_2.pack(pady=8)
RE9_2.place(x=330,y=2980)

telechargementRE9_3=PhotoImage(file="./fenetre1/REBA/reba/re9_3.png")
RE9_3=Radiobutton(second_frame, image=telechargementRE9_3,fg="blue",var=radio_17,value=3,command=com_RE9,bg="white",activebackground="white")
RE9_3.pack(pady=8)
RE9_3.place(x=580,y=2980)

label_12=Label(second_frame,text="Score de l'ajustement de la position du poignet :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_12.pack()
label_12.place(x=280,y=3200)

telechargementRE_Ajust9_1=PhotoImage(file="./fenetre1/REBA/reba/Re9_Ajus9_1.png")
RE_Ajust9_1=Checkbutton(second_frame, image=telechargementRE_Ajust9_1,fg="blue",var=radio_18,command=com_RE9_Ajust,bg="white",activebackground="white")
RE_Ajust9_1.pack(pady=8)
RE_Ajust9_1.place(x=200,y=3250)

telechargementRE_Ajust9_2=PhotoImage(file="./fenetre1/REBA/reba/re9_Ajus9_2.png")
RE_Ajust1_2=Checkbutton(second_frame, image=telechargementRE_Ajust9_2,fg="blue",var=radio_19,command=com_RE9_Ajust,bg="white",activebackground="white")
RE_Ajust1_2.pack(pady=8)
RE_Ajust1_2.place(x=480,y=3250)

   #Etape 11 : score de la facilité de prise

label_13=Label(second_frame,text="Score de la facilité de la prise :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_13.pack()
label_13.place(relx=0.5,y=3470,anchor=CENTER)

RE11_1=Radiobutton(second_frame, text="La saisie est bonne avec des poignées  ",fg="black",var=radio_20,value=1,command=SE_11,bg="white",activebackground="white")
RE11_1.pack(pady=8)
RE11_1.place(x=40,y=3520)


RE11_2=Radiobutton(second_frame, text="La prise est acceptable",fg="black",var=radio_20,value=2,command=SE_11,bg="white",activebackground="white")
RE11_2.pack(pady=8)
RE11_2.place(x=550,y=3520)

RE11_3=Radiobutton(second_frame, text="La prise n’est pas acceptable/presque pas possible ",fg="black",var=radio_20,value=3,command=SE_11,bg="white",activebackground="white")
RE11_3.pack(pady=8)
RE11_3.place(x=40,y=3570)

RE11_4=Radiobutton(second_frame, text="La prise est dangereuse ",fg="black",var=radio_20,value=4,command=SE_11,bg="white",activebackground="white")
RE11_4.pack(pady=8)
RE11_4.place(x=550,y=3570)

   #Etape 14 : score d'activité

label_14=Label(second_frame,text="Score d'activité :",font=("Times New Roman",15),fg="black",bg="white",activebackground="white")
label_14.pack()
label_14.place(relx=0.5,y=3650,anchor=CENTER)


RE14_1=Checkbutton(second_frame,text= "La posture est statique (tenue>1min)" ,fg="black",var=radio_21,command=SE_14,bg="white",activebackground="white")
RE14_1.pack(pady=8)
RE14_1.place(x=40,y=3700)

RE14_2=Checkbutton(second_frame,text= "La posture est répétée plus de 4 fois par minutes",fg="black",var=radio_22,command=SE_14,bg="white",activebackground="white")
RE14_2.pack(pady=8)
RE14_2.place(x=550,y=3700)

RE14_3=Checkbutton(second_frame,text= "Rapidité et large changement de posture ou une base instable" ,fg="black",var=radio_23,command=SE_14,bg="white",activebackground="white")
RE14_3.pack(pady=8)
RE14_3.place(x=250,y=3750)

   #Boutons

telechargement_check=PhotoImage(file="./fenetre1/REBA/check.png")
button_1=Button(second_frame,image=telechargement_check,fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=check)
button_1.pack()
button_1.place(relx=0.5,y=3840,anchor=CENTER)
button_1.bind_all('<Key>',press)

telechargement_precedent1=PhotoImage(file="./fenetre1/REBA/precedent.png")
button_2=Button(second_frame,image=telechargement_precedent1,fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=precedent)
button_2.pack()
button_2.place(x=100,y=3810)

telechargement_precedent2=PhotoImage(file="./fenetre1/REBA/precedent.png")
button_21=Button(second_frame,image=telechargement_precedent2,fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=precedent)
button_21.pack()
button_21.place(x=20,y=30)

telechargement_quitter=PhotoImage(file="./fenetre1/REBA/quitter.png")
button_3=Button(second_frame,image=telechargement_quitter,fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=quitter)
button_3.pack()
button_3.place(x=749,y=3810)

telechargement_angle=PhotoImage(file="./fenetre1/REBA/angle.png")
button_4=Button(second_frame,image=telechargement_angle,fg="white",width=60,height=60,border="0",bg="white",activebackground="white",command=angle_fn)
button_4.pack()
button_4.place(x=800,y=30)

second_frame.configure(height=3910)
window.mainloop()
