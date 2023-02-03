#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 09:18:04 2023

@author: tallakbertin
"""

from tkinter import *
window = Tk() #Instantiate an instance of a window
popup = Tk()
popup.title("Kryptering Ut")
window.geometry("960x540")
window.title("Krypteringsprogram GUI")
window.config(background="#61cf7b")

# ikon = PhotoImage(file='')
# window.iconphoto(True, "Navn på ikon")

#photo = PhotoImage(file='')
# argument i label image=photo, compund='bottom')

label = Label(window,text="Dette programmet skal kryptere og dekryptere tekst",
              font=("Arial",24,"bold"),
              relief=RAISED,
              bd=10,
              padx=30)        #Forklaring
label.pack()                  
entry1 = Entry(window)
entry1.insert(0,'melding til kryptering')
entry1.pack()                 #inputvindu
entry2 = Entry(window)
entry2.insert(0,'alfabet til dekryptering')
entry2.pack()
entry3 = Entry(window)
entry3.insert(0,'nøkkel til kryptering')
entry3.pack()
def krypter():
    budskap = entry1.get()
    import string_utils                                   #Alfabetisk randomizer
    alfabet = string_utils.shuffle(" abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ.,:;-_?!/")
    import random                                         #Randomiser for kryptnøkkel
    f = random.randint(1,len(alfabet))
    kryptering = f
    kryptering = int(kryptering)
    budskap = entry1.get()         #Tar melding til krypt fra entry1
    output = ""                                           #Outputplaceholder
    def encode(bokstav, kryptering):                      #Enkoderfunksjon
        pos = alfabet.find(bokstav) 
        nypos = (pos + kryptering)
        if nypos >= len(alfabet):
            nypos = nypos - len(alfabet)
        return alfabet[nypos]
    for bokstav in budskap:                               #Enkodermodul
        if bokstav in alfabet:
            output = output + encode(bokstav, kryptering)
        else:
            output = output + bokstav
    kryptering = str(kryptering)
    messageboks1 = Text(popup, height=2, borderwidth=0)
    messageboks1.insert(1.0,"Det originale budskapet: "+budskap+" . !Bør ikke sendes som melding, da er poenget borte!")
    messageboks1.pack()
    messageboks1.config(state="normal")
    messageboks2 = Text(popup, height=2, borderwidth=0)
    messageboks2.insert(1.0,"Det krypterte budskapet !etter første bindestrek!:-"+output)
    messageboks2.pack()
    messageboks2.config(state="normal")
    messageboks3 = Text(popup, height=2, borderwidth=0)
    messageboks3.insert(1.0,"Kryoteringsnøkkelen: "+kryptering)
    messageboks3.pack()
    messageboks3.config(state="normal")
    messageboks4 = Text(popup, height=2, borderwidth=0)
    messageboks4.insert(1.0,"Den genererte alfabetet !etter første bindestrek!:-"+alfabet)
    messageboks4.pack()
    messageboks4.config(state="normal")
    output0 = Label(window, text="Det originale budskapet er: "+budskap)
    output0.pack()
    output1 = Label(window,text="krypteringen er: "+ output)
    output1.pack()
    output2 = Label(window,text="Krypteringsnøkkelen er: "+ kryptering)         #Print kryptnøkkel
    output2.pack()
    output3 = Label(window,text="Alfabetet generert er: "+ alfabet)
    output3.pack()
    entry1.delete(0,END)
    entry1.insert(0,output)
    entry2.delete(0,END)
    entry2.insert(0,alfabet)
    entry3.delete(0,END)
    entry3.insert(0,kryptering)
    output0.after(20000,output0.destroy)
    output1.after(20000,output1.destroy)
    output2.after(20000,output2.destroy)
    output3.after(20000,output3.destroy)
def dekrypter():
    alfabet = entry2.get()
    kryptering = entry3.get()                   #Input på kryptnøkkel
    kryptering = int(kryptering)
    budskap = entry1.get()                      #Input på kryptert meld
    output = ""                             #outputplaceholder
    def decode(bokstav, kryptering):                      #Dekoderfunksjon
        pos = alfabet.find(bokstav) 
        nypos = (pos - kryptering)
        if nypos < 0:
            nypos = nypos + (len(alfabet))
        return alfabet[nypos]
    for bokstav in budskap:                               #Dekodermodul
        if bokstav in alfabet:
            output = output + decode(bokstav, kryptering)
        else:
            output = output + bokstav
    messagebox5 = Label(popup,text="Her er det dekrypterte budskapet: "+output)
    messagebox5.pack()
    output4 = Label(window,text="Dekrypteringen er: "+ output)
    output4.pack()
    output4.after(20000, output4.destroy)
def empty():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
def kill():
    window.destroy()
    popup.destroy()
    
button1 = Button(window,            #Velg kryptering
                 text="Krypter",
                 command = krypter,
                 activeforeground="light blue",
                 activebackground="white")
button1.pack()

button2 = Button(window,          #Velg dekryptering
                 text="Dekrypter",
                 command = dekrypter,
                 activeforeground="light blue",
                 activebackground="white")
button2.pack()

buttontoem = Button(window,text="Tøm alle bokser",command=empty)  #Tøm felt
buttontoem.pack()

buttonkill = Button(window, text="Lukk program",command=kill)     #Lukk program (På Windows)
buttonkill.pack(side=BOTTOM)
popup.mainloop()
window.mainloop() #Plasserer vindu, se etter event