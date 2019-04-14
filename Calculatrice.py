#! /usr/bin/env python3
# coding: utf-8

import sys

from tkinter import *

###########################################################################################
######################       EXERCICE SANS GRID         ###################################
###########################################################################################

fenetre = Tk()   # ceci est la fenetre principale --->  Tk()

###########################################################################################
###########################################################################################


# FONCTION "C" pour effacer le champs d'affichage, l'écran de la calculatrice :
#------------------------------------------------------------------------------
def clear():
  global operator
  operator = ""
  entree.set("")


# FONCTION d'affichage des chiffres :
#------------------------------------
def boutonClic(numbers):
  global operator
  operator = operator + str(numbers)
  entree.set(operator)


# FONCTION d'égalité :
#-----------------------------------------------------------------------------------------------
def boutonEgale():
  global operator
  sumup = str(eval(operator))
  entree.set(sumup)
  operator = ""



operator = ""


entree = StringVar()    # indispensable pour donner un caractère dans le champs
                        # d'affichage (numérique ou alphabétique ou opérateur +x:- ou autres...)

###########################################################################################
###########################################################################################


fenetre.geometry("1000x700+0+0")  # 1000 x 700 = c'est la taille de la fenêtre.
                                  # Sinon sans problème la fenetre s'ouvre à la bonne taille,
                                  # mais ça peut être pratique de faire plus grand pour
                                  # recouvrir un peu l'écran et concentrer l'attention sur 
                                  # le jeu. 0 + 0 c'est la distance entre la fenetre et le
                                  # bord gauche et haut de l'écran.
                                  
frame = Frame(fenetre)
frame.pack()


fenetre.title("CALCULATRICE - Vincent N")

###########################################################################################
###########################################################################################

label = Label(fenetre, text = "---------Calculatrice simple format ---------", bg="coral")
label.pack()

###############     RANGEE Afficheur     ###########################################

txtDisplay = Entry(frame, textvariable = entree, bd=28, insertwidth = 1,
                   font = 30, bg = "azure")
txtDisplay.pack(side = TOP)


##############        1iere RANGEE      ############################################

premierframe = Frame(fenetre)
premierframe.pack(side = TOP)


boutonEgale = Button(premierframe, padx = 16, pady = 16, bd = 8, text = "=", fg = "blue",
                     bg = "orange", activebackground="coral", command = boutonEgale)
boutonEgale.pack(side = LEFT)


boutonClear = Button(premierframe, padx = 16, pady = 16, bd = 8, text = "C", fg = "blue",
                     bg = "orange", activebackground="coral", command = clear)
boutonClear.pack(side = LEFT)


boutonParentheseAGauche = Button(premierframe, padx = 17, pady = 16, bd = 8, text = "(",
                                 fg = "blue", bg = "orange", activebackground="coral",
                                 command = lambda:boutonClic("("))
boutonParentheseAGauche.pack(side = LEFT)


boutonParentheseADroite = Button(premierframe, padx = 17, pady = 16, bd = 8, text = ")",
                                 fg = "blue", bg = "orange", activebackground="coral",
                                 command = lambda:boutonClic(")"))
boutonParentheseADroite.pack(side = LEFT)


##############        2eme RANGEE       ############################################

secondframe = Frame(fenetre)
secondframe.pack(side = TOP)


bouton1 = Button(secondframe, padx = 17, pady = 16, bd = 8, text = "1",
                 fg = "blue", bg = "orange", activebackground="green",
                 command = lambda:boutonClic(1))
bouton1.pack(side = LEFT)


bouton2 = Button(secondframe, padx = 16, pady = 16, bd = 8, text = "2",
                 fg = "blue", bg = "orange", activebackground="green",
                 command = lambda:boutonClic(2))
bouton2.pack(side = LEFT)


bouton3 = Button(secondframe, padx = 16, pady = 16, bd = 8, text = "3",
                 fg = "blue", bg = "orange", activebackground="green",
                 command = lambda:boutonClic(3))
bouton3.pack(side = LEFT)


boutonFois = Button(secondframe, padx = 16, pady = 16, bd = 8, text = "x",
                    fg = "blue", bg = "orange", activebackground="purple",
                    command = lambda:boutonClic("*"))
boutonFois.pack(side = LEFT)


##############        3eme RANGEE       ############################################

troisiemeframe = Frame(fenetre)
troisiemeframe.pack(side = TOP)


bouton4 = Button(troisiemeframe, padx = 16, pady = 16, bd = 8, text = "4",
                 fg = "blue", bg = "orange", activebackground="green",
                 command = lambda:boutonClic(4))
bouton4.pack(side = LEFT)


bouton5 = Button(troisiemeframe, padx = 16, pady = 16, bd = 8, text = "5",
                 fg = "blue", bg = "orange", activebackground="green",
                 command = lambda:boutonClic(5))
bouton5.pack(side = LEFT)


bouton6 = Button(troisiemeframe, padx = 16, pady = 16, bd = 8, text = "6",
                 fg = "blue", bg = "orange", activebackground="green",
                 command = lambda:boutonClic(6))
bouton6.pack(side = LEFT)


boutonDivise = Button(troisiemeframe, padx = 17, pady = 16, bd = 8, text = ":",
                      fg = "blue", bg = "orange", activebackground="purple",
                      command = lambda:boutonClic("/"))
boutonDivise.pack(side = LEFT)


##############        4eme RANGEE       ############################################

quatriemeframe = Frame(fenetre)
quatriemeframe.pack(side = TOP)


bouton7 = Button(quatriemeframe, padx = 16, pady = 16, bd = 8, text = "7",
                 fg = "blue", bg = "orange", activebackground="green",
                 command = lambda:boutonClic(7))
bouton7.pack(side = LEFT)


bouton8 = Button(quatriemeframe, padx = 16, pady = 16, bd = 8, text = "8",
                 fg = "blue", bg = "orange", activebackground="green",
                 command = lambda:boutonClic(8))
bouton8.pack(side = LEFT)


bouton9 = Button(quatriemeframe, padx = 16, pady = 16, bd = 8, text = "9",
                 fg = "blue", bg = "orange", activebackground="green",
                 command = lambda:boutonClic(9))
bouton9.pack(side = LEFT)


boutonPlus = Button(quatriemeframe, padx = 15, pady = 16, bd = 8, text = "+",
                    fg = "blue", bg = "orange", activebackground="purple",
                    command = lambda:boutonClic("+"))
boutonPlus.pack(side = LEFT)


##############        5eme RANGEE       ############################################

cinquiemeframe = Frame(fenetre)
cinquiemeframe.pack(side = TOP)


boutonZero = Button(cinquiemeframe, padx = 46, pady = 16, bd = 8, text = "0",
                    fg = "blue", bg = "orange", activebackground="green",
                    command = lambda:boutonClic(0))
boutonZero.pack(side = LEFT)


boutonVirgule = Button(cinquiemeframe, padx = 17, pady = 16, bd = 8, text = ".",
                       fg = "blue", bg = "orange", activebackground="coral",
                       command = lambda:boutonClic("."))
boutonVirgule.pack(side = LEFT)


boutonMoins = Button(cinquiemeframe, padx = 17, pady = 16, bd = 8, text = "-",
                     fg = "blue", bg = "orange", activebackground="purple",
                     command = lambda:boutonClic("-"))
boutonMoins.pack(side = LEFT)


###########################################################################################
###########################################################################################

fenetre.mainloop()
