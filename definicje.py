# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:58:37 2019

@author: XX
"""

import numpy as np
import sys
import matplotlib.pyplot as plt

"""
sprawdzenie czy wprowadzone dane są danymi liczbowymi i wymuszenie poprawnych danych
"""
def Xa(XA):
    a=XA.lstrip('-').replace(".", '',1).isdigit() #sprawdzenie czy podane dane są liczbą
    if a==True:
        Xa=float(XA) # jesli tak to zmienienie jej w wartosć typu float
    else:
        XA=input("podaj XA jako liczbę") # jesli nie to prosba użytkownika o podanie nowych danych
        a=XA.lstrip('-').replace(".", '',1).isdigit()
        if a==False: # jesli dane znów nie są liczbą zakończenie działania programu 
            sys.exit("Dwukrotnie podano złą wartosć, nie rozpoczęto obliczeń")
        else:
            Xa=float(XA)
            
    return(Xa) # funkcja zwraca wartosc współrzędnej Xa jako float 
    
    
def Ya(YA):      
    aa=YA.lstrip('-').replace(".", '',1).isdigit()
    if aa==True:
        Ya=float(YA)
    else:
        YA=input("podaj YA jako liczbę")
        aa=YA.lstrip('-').replace(".", '',1).isdigit()
        if aa==False:
            sys.exit("Dwukrotnie podano złą wartosć, nie rozpoczęto obliczeń")
        else:
            Ya=float(YA)
    return(Ya)
 
def Xb(XB):   
    b=XB.lstrip('-').replace(".", '',1).isdigit()
    if b==True:
        Xb=float(XB)
    else:
        XB=input("podaj XB jako liczbę")
        b=XB.lstrip('-').replace(".", '',1).isdigit()
        if b==False:
            sys.exit("Dwukrotnie podano złą wartosć, nie rozpoczęto obliczeń")
        else:
            Xb=float(XB)
    return(Xb)
    
def Yb(YB):    
    bb=YB.lstrip('-').replace(".", '',1).isdigit()
    if bb==True:
        Yb=float(YB)
    else:
        YB=input("podaj YB jako liczbę")
        bb=YB.lstrip('-').replace(".", '',1).isdigit()
        if bb==False:
            sys.exit("Dwukrotnie podano złą wartosć, nie rozpoczęto obliczeń")
        else:
            Yb=float(YB)
    return(Yb)
    
def Xc(XC):
    c=XC.lstrip('-').replace(".", '',1).isdigit()
    if c==True:
        Xc=float(XC)
    else:
        XC=input("podaj XC jako liczbę")
        c=XC.lstrip('-').replace(".", '',1).isdigit()
        if c==False:
            sys.exit("Dwukrotnie podano złą wartosć, nie rozpoczęto obliczeń")
        else:
            Xc=float(XC)
    return(Xc)
    
def Yc(YC):
    cc=YC.lstrip('-').replace(".", '',1).isdigit()
    if cc==True:
        Yc=float(YC)
    else:
        YC=input("podaj YC jako liczbę")
        cc=YC.lstrip('-').replace(".", '',1).isdigit()
        if cc==False:
            sys.exit("Dwukrotnie podano złą wartosć, nie rozpoczęto obliczeń")
        else:
            Yc=float(YC)
    return(Yc)   
    
def Xd(XD):   
    d=XD.lstrip('-').replace(".", '',1).isdigit()
    if d==True:
        Xd=float(XD)
    else:
        XD=input("podaj XD jako liczbę")
        d=XD.lstrip('-').replace(".", '',1).isdigit()
        if d==False:
            sys.exit("Dwukrotnie podano złą wartosć, nie rozpoczęto obliczeń")
        else:
            Xd=float(XD)
    return(Xd)

def  Yd(YD):    
    dd=YD.lstrip('-').replace(".", '',1).isdigit()
    if dd==True:
        Yd=float(YD)
    else:
        YD=input("podaj YD jako liczbę")
        dd=YD.lstrip('-').replace(".", '',1).isdigit()
        if dd==False:
            sys.exit("Dwukrotnie podano złą wartosć, nie rozpoczęto obliczeń")
        else:
            Yd=float(YD)
    return(Yd)

"""
Współrzędne punktu przecięcia
"""

def M1(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd): # wyznaczenie mianownika dla parametrów pomocniczych t1  i t2
    m1=((Xb-Xa)*(Yd-Yc)-(Yb-Ya)*(Xd-Xc))
    return(m1)
    
def wspPX(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd,m1): # obliczenie współrzędnej X punktu A
    if m1==0: # jesli mianownik parametrów jest równy zero to oznacza, ze punkt przecięcia nie istnieje zatem nie ma jego współrzędnych, program zwraca '--'
        Xp1='--'
    else:
        t1=((Xc-Xa)*(Yd-Yc)-(Yc-Ya)*(Xd-Xc))/m1 # jeli parametry istnieją to obliczane są współrzędne punktu P
        t2=((Xc-Xa)*(Yb-Ya)-(Yc-Ya)*(Xb-Xa))/m1
        Xp1=Xa+t1*(Xb-Xa)
    return("{:.3f}".format(Xp1)) # zwracanie współrzędnej z odpowiednią dokładnocią miejsc po przecinku 

def wspPY(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd,m1):
    if m1==0:
        Yp1='--'
    else:
        t1=((Xc-Xa)*(Yd-Yc)-(Yc-Ya)*(Xd-Xc))/m1
        t2=((Xc-Xa)*(Yb-Ya)-(Yc-Ya)*(Xb-Xa))/m1
        Yp1=Ya+t1*(Yb-Ya)
    return("{:.3f}".format(Yp1))
"""
Położenie punktu P względem odcinków i zapis współrzędnych do pliku 
"""
def gdzie(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd,m1):     
    if m1==0: 
        w="Punkt przecięcia nie istnieje" # jesli mianownik parametrów jest równy 0, to nie ma punktu przecięcia, a więc nie ustalimy jego położenia
    else:
        t1=((Xc-Xa)*(Yd-Yc)-(Yc-Ya)*(Xd-Xc))/m1
        t2=((Xc-Xa)*(Yb-Ya)-(Yc-Ya)*(Xb-Xa))/m1
        Xp1=Xa+t1*(Xb-Xa)
        Yp1=Ya+t1*(Yb-Ya)
        plik2= open('Współrzędne punktu P.txt', "a") # zapis współrzędnych do pliku 
        plik2.write("\n| {:^14} | {:^14} |\n ".format("XP","YP")); # zapis współrzędnych z odpowiednimi nagłówkami oraz z odpowiednią iloscią miejsc po przecinku
        plik2.write("\n|{:^16.3f}|{:^16.3f}|\n".format(Xp1,Yp1))
        if 0<=t1<=1 and 0<=t2<=1: # okrelslenie położenia punktu przecięcia względem odcinków
            w="Punkt P leży na przecięciu odcinków (należy do obu)"
        else:
            w="Punkt P  leży na przedłużeniu jednego lub obu odcinków"
    return(w)
"""
Położenie punktów C i D względem odcinka AB
"""
def polC(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd):
    DetC=Xa*Yb+Xb*Yc+Xc*Ya-Xc*Yb-Xa*Yc-Xb*Ya  # obliczenie wyznacznika
    if DetC>0: # okreslenie na podstawie wartosci wyznacznika połozenia punktu 
        gdz="Punkt C leży po prawej stronie odcinka AB "
    elif DetC<0:
        gdz="Punkt C leży po lewej stronie odcinka AB"
    else:
        gdz="Punkt C jest współliniowy z odcinkiem AB" 
    return(gdz)
def polD(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd):    
    DetD=Xa*Yb+Xb*Yd+Xd*Ya-Xd*Yb-Xa*Yd-Xb*Ya
    if DetD>0:
        gdzD="Punkt D leży po prawej stronie odcinka AB "
    elif DetD<0:
        gdzD="Punkt D leży po lewej stronie odcinka AB"
    else:
        gdzD="Punkt D jest współliniowy z odcinkiem AB" 
    return(gdzD)

"""
Azymut odcinka AB
"""
import math

def Azymut(Xa,Xb,Ya,Yb):
    dX=Xb-Xa # obliczenie różnic między wsopółrzędnymi
    dY=Yb-Ya
    odl= float(math.sqrt(dX**2+dY**2)) # obliczenieodległosci między punktami
    if dY>0 and dX>0: # okreslenie ćwiartki 
        az= math.atan(dY/dX) # obliczenie azymutu 
        az_deg = math.degrees(az) # przedstawienie azymutu w stopniach 
    elif dY>0 and dX<0:
        az= math.atan(dY/dX)+ math.pi
        az_deg = math.degrees(az)
    elif dY<0 and dX<0:
        az= math.atan(dY/dX)+ math.pi
        az_deg = math.degrees(az)
    elif dY<0 and dX>0:
        az= math.atan(dY/dX)+ 2*math.pi
        az_deg = math.degrees(az)
    elif dY>0 and dX==0:
        az_deg = 90
    elif dY==0 and dX<0:
        az_deg = 180    
    elif dY<0 and dX==0:
        az_deg = 270
    elif dY==0 and dX>0:
        az_deg = 360
    elif dY==0 and dX==0:
        az_deg=0
    return("{:.3f}".format(az_deg))
    
"""
Odległ○c punktu P od punktów A, B, C, D
"""
def odlA(Xa,Xp1,Ya,Yp1):
    if Xp1=='--': # nie da się okreslić odległoci jesli punkt P nie istnieje 
        odlA='--'
    else:
        Xp1=float(Xp1) # zamiana współrzędnych punktu P na float
        Yp1=float(Yp1)
        odlA= float(math.sqrt((Xa-Xp1)**2+(Ya-Yp1)**2))  # obliczenie odległoci między punktami 
    return("{:.3f}".format(odlA));

def odlB(Xb,Xp1,Yb,Yp1):
    if Xp1=='--':
        odlB='--'
    else:
        Xp1=float(Xp1)
        Yp1=float(Yp1)
        odlB= float(math.sqrt((Xb-Xp1)**2+(Yb-Yp1)**2)) 
    return("{:.3f}".format(odlB));

def odlC(Xc,Xp1,Yc,Yp1):
    if Xp1=='--':
        odlC='--'
    else:
        Xp1=float(Xp1)
        Yp1=float(Yp1)
        odlC= float(math.sqrt((Xc-Xp1)**2+(Yc-Yp1)**2)) 
    return("{:.3f}".format(odlC));

def odlD(Xd,Xp1,Yd,Yp1):
    if Xp1=='--':
        odlD='--'
    else:
        Xp1=float(Xp1)
        Yp1=float(Yp1)
        odlD= float(math.sqrt((Xd-Xp1)**2+(Yd-Yp1)**2)) 
    return("{:.3f}".format(odlD));

"""
WYKRES
"""
    
def wykres(Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd,Xp1,Yp1,kolor1,kolor2):
    if Xp1=='--': # jeli punkt P nie istnieje, wykres ryswoany bez tego punktu 
        plt.plot([Xa,Xb], [Ya,Yb], color=kolor1, label='odcinek AB') # rysowanie odcinka AB, jego kolor i etykieta
        plt.plot([Xc,Xd], [Yc,Yd], color=kolor2, label= "odcinek CD")  # rysowanie odcinka CD, jego kolor i etykieta
        plt.xlabel("X[m]") # nazwanie osi i podanie jednostek
        plt.ylabel("Y[m]")
        plt.scatter(Xa,Ya, label='Punkt A [ {:.2f},{:.2f}]'.format(Xa, Ya), color="lime") # rysowanie punktu A, jego kolor, etykieta i współrzędne
        plt.scatter(Xb,Yb, label='Punkt B[ {:.2f},{:.2f}]'.format(Xb, Yb), color="aqua")
        plt.scatter(Xc,Yc, label='Punkt C [ {:.2f},{:.2f}]'.format(Xc, Yc), color="silver")
        plt.scatter(Xd,Yd, label='Punkt D[ {:.2f},{:.2f}]'.format(Xd, Yd), color="plum")
        plt.legend()
    else:
        Xp1=float(Xp1) # zamiana współrzędnych punktu P na float
        Yp1=float(Yp1)
        plt.plot([Xa,Xp1], [Ya,Yp1], '--', color=kolor1) # rysowanie linii będących przedłużeniem odcinków, jesli punkt P leży na przedłużeniu 
        plt.plot([Xc,Xp1], [Yc,Yp1], '--', color=kolor2)
        plt.plot([Xa,Xb], [Ya,Yb], color=kolor1, label='odcinek AB') # rysowanie odcinka AB, jego kolor i etykieta
        plt.plot([Xc,Xd], [Yc,Yd], color=kolor2, label= "odcinek CD")
        plt.xlabel("X[m]") # nazwanie osi i podanie jednostek
        plt.ylabel("Y[m]")
        plt.scatter(Xp1,Yp1, s=75, label='Punkt P [ {:.2f},{:.2f}]'.format(Xp1, Yp1)) # rysowanie punktu P, jego kolor, etykieta i współrzędn
        plt.scatter(Xa,Ya, s=75, label='Punkt A [ {:.2f},{:.2f}]'.format(Xa, Ya), color="lime")
        plt.scatter(Xb,Yb, s=75, label='Punkt B[ {:.2f},{:.2f}]'.format(Xb, Yb), color="aqua")
        plt.scatter(Xc,Yc, s=75, label='Punkt C [ {:.2f},{:.2f}]'.format(Xc, Yc), color="silver")
        plt.scatter(Xd,Yd, s=75, label='Punkt D[ {:.2f},{:.2f}]'.format(Xd, Yd), color="plum")
        plt.legend()
    

    return(plt)





