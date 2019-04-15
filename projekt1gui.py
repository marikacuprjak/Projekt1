# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 08:12:51 2019

@author: XX
"""

import tkinter as tk #zaimportowanie odpowiednich bibliotek i plików z napisanym programem obliczeniowym
from tkinter import *
from definicje import *


def przelicz(okno_rodzic,pole1,pole2,pole3,pole4,pole5,pole6,pole7,pole8,pole9,pole10): # definicja okien projektwanej aplikacji oraz wartosci wpisywanych do aplikacji
  okno=tk.Toplevel(okno_rodzic,background="powderblue") #projekt okna z wynikami, tło, tytuł
  okno.title('Wyniki')
  p1=(pole1.get()) #XA,zdefiniowanie pól, do których będą wpisywane dane podane przez użytkownika
  p2=(pole2.get()) #YA
  p3=(pole3.get()) #XB
  p4=(pole4.get()) #YB
  p5=(pole5.get()) #XC
  p6=(pole6.get()) #YC
  p7=(pole7.get()) #XD
  p8=(pole8.get()) #YD
  kolor=str(pole9.get()) # kolor odcinka AB
  kolor1=str(pole10.get()) # kolor odcinka CD
  xa=float(Xa(p1))#sprawdzenie czy wprowadzone dane są danymi liczbowymi i wymuszenie poprawnych danych
  ya=float(Ya(p2))
  xb=float(Xb(p3))
  yb=float(Yb(p4))
  xc=float(Xc(p5))
  yc=float(Yc(p6))
  xd=float(Xd(p7))
  yd=float(Yd(p8))
  m1=float(M1(xa,ya,xb,yb,xc,yc,xd,yd)) #definicja wartosci ukazywanych w oknie wynikowym, używanie zdefiniowanych programów obliczeniowych,
  XP=str(wspPX(xa,ya,xb,yb,xc,yc,xd,yd,m1)) #Współrzędna x punktu P
  YP=str(wspPY(xa,ya,xb,yb,xc,yc,xd,yd,m1)) #Współrzędna y punktu P
  gdzieP=str(gdzie(xa,ya,xb,yb,xc,yc,xd,yd,m1)) # położenie punktu P względem odcinków
  gdzieC=str(polC(xa,ya,xb,yb,xc,yc,xd,yd)) # położenie punktu C względem odcinka AB
  gdzieD=str(polD(xa,ya,xb,yb,xc,yc,xd,yd)) # położenie punktu D względem odcinka AB
  AzAB=str(Azymut(xa,xb,ya,yb)) #Azymut odcinka AB
  odlA1=str(odlA(xa,XP,ya,YP)) # odległoc punktu A od punktu P
  odlB1=str(odlA(xb,XP,yb,YP)) # odległoc punktu B od punktu P
  odlC1=str(odlA(xc,XP,yc,YP)) # odległoc punktu C od punktu P
  odlD1=str(odlA(xd,XP,yd,YP)) # odległoc punktu D od punktu P
  wykres1=(wykres(xa,ya,xb,yb,xc,yc,xd,yd,XP,YP,kolor,kolor1)) # wykres 
  tk.Label(okno, text="Współrzędne X punktu P:  "+XP + "m",background="powderblue").pack() #zdefiniowanie wyglądu okienek w oknie wynikowym jako nazwa+wynik na podstawie zdefiniowanego wyżej przeliczenia
  tk.Label(okno, text="Współrzędna Y punktu P :  "+YP +"m",background="powderblue").pack()
  tk.Label(okno, text= gdzieP ,background="powderblue").pack()
  tk.Label(okno, text=gdzieC,background="powderblue").pack()
  tk.Label(okno, text= gdzieD,background="powderblue").pack()
  tk.Label(okno, text="Azymut odcinka AB:  "+AzAB +"stopni",background="powderblue").pack()
  tk.Label(okno, text="Odległosć punktu A od punktu P: " +odlA1 +"m",background="powderblue").pack()
  tk.Label(okno, text="Odległosć punktu B od punktu P: " +odlB1 +"m",background="powderblue").pack()
  tk.Label(okno, text="Odległosć punktu C od punktu P: " +odlC1 + "m",background="powderblue").pack()
  tk.Label(okno, text="Odległosć punktu D od punktu P: " +odlD1 + "m",background="powderblue").pack()
  tk.Canvas(okno, wykres1).pack() # wygenerowanie rysowania wykresu 

# dodawanie widgetów, fubnkcjonalnosc, zmiana wygladu, uruchomienie petli zdarzen
root = tk.Tk() # okno główne
root.title("Wpisz współrzędne punktów")

#dodawanie widgetów
l1 = tk.Label(root, text="XA")  # widget tekstowy opisujący do czego odnosi się wpisywana wartosć
e1 = tk.Entry(root, width = 15,background="peachpuff") # okno, do którego użytkownik wpisuje okresloną wielkosć, zdefiniowanie koloru tego okienka i jego rozmiaru
l2 = tk.Label(root, text="YA")
e2 = tk.Entry(root, width = 15,background="peachpuff")
l3 = tk.Label(root, text="XB")
e3 = tk.Entry(root, width = 15,background="peachpuff") 
l4 = tk.Label(root, text="YB")
e4 = tk.Entry(root, width = 15,background="peachpuff")
l5 = tk.Label(root, text="XC")
e5 = tk.Entry(root, width = 15,background="peachpuff") 
l6 = tk.Label(root, text="YC")
e6 = tk.Entry(root, width = 15,background="peachpuff")
l7 = tk.Label(root, text="XD")
e7= tk.Entry(root, width = 15,background="peachpuff")
l8 = tk.Label(root, text="YD")
e8= tk.Entry(root, width = 15,background="peachpuff")
l9 = tk.Label(root, text="Wpisz kolor dla odcinka AB")
e9= tk.Entry(root, width = 15,background="palegreen")
l10 = tk.Label(root, text="Wpisz kolor dla odcinka CD")
e10= tk.Entry(root, width = 15,background="palegreen")

def clear(pole1,pole2,pole3,pole4,pole5,pole6,pole7,pole8,pole9,pole10): # czyszczenie okien wpisywania danych 
    pole1.delete(0,'end')
    pole2.delete(0,'end')
    pole3.delete(0,'end')
    pole4.delete(0,'end')
    pole5.delete(0,'end')
    pole6.delete(0,'end')
    pole7.delete(0,'end')
    pole8.delete(0,'end')
    pole9.delete(0,'end')
    pole10.delete(0,'end')
 

    


#przycisk wywołujący przeliczenia, jego kolor, tekst na nim, rozmiar
#command = lambda:nowe(root)  
#lambda aby podac argumenty funkcji
b1 = tk.Button(root, width=20, text="Oblicz",bg='salmon', command =lambda:przelicz(root,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10))  #przycisk i metoDA,napisanie żeby dodało e1 i e2 
b2 = tk.Button(root, width=20, text="Wyczysć",bg='salmon', command =lambda:clear(e1,e2,e3,e4,e5,e6,e7,e8,e9,e10)) # przycisk do czyszczenia danych
#rozmieszczenie widgetów
# grid rozmiescza, lokalizuje okrelony widget według podanego wiersza(row) i kolumny(column)

l1.grid(row=0, column=0) # np widget 1 czyli tekst"XA" będzie w pierwszym wierszu i w pierwszej kolumnie
e1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e2.grid(row=1, column=1)
l3.grid(row=0, column=2)
e3.grid(row=0, column=3)
l4.grid(row=1, column=2)
e4.grid(row=1, column=3)
l5.grid(row=0, column=4)
e5.grid(row=0, column=5)
l6.grid(row=1, column=4)
e6.grid(row=1, column=5)
l7.grid(row=0, column=6)
e7.grid(row=0, column=7)
l8.grid(row=1, column=6)
e8.grid(row=1, column=7)
l9.grid(row=3, column=0)
e9.grid(row=3, column=1)
l10.grid(row=4, column=0)
e10.grid(row=4, column=1)
b1.grid(row=5, column=3) #loklizacja przycisku
b2.grid(row=5, column=5)
#uruchamia petle wydarzen!
root.mainloop()
