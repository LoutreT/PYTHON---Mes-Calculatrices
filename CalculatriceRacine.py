# Cette fois-ci, je vais faire des menus déroulables avec la souris, programmés à la fin, tout en bas : 


from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Calculatrice Racine Carree")
root.configure(background = "powder blue")
root.resizable(width = False, height = False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

class Calc():
  def __init__(self):
    self.total = 0
    self.current = ""
    self.input_value = True
    self.check_sum = False
    self.op = ""
    self.result = False

  def numberEnter(self, num):
    self.result = False
    firstnum = txtDisplay.get()#################### A controler Diaplay
    secondnum = str(num)
    if self.input_value:
      self.current = secondnum
      self.input_value = False
    else :
      if secondnum == '.':
        if secondnum in firstnum:
          return
      self.current = firstnum + secondnum
    self.display(self.current)

  def sum_of_total(self):
    self.result = True
    self.current = float(self.current)
    if self.check_sum == True:
      self.valid_function()
    else:
      self.total = float(txtDisplay.get())

  def display(self, value):
    txtDisplay.delete(0, END)
    txtDisplay.insert(0, value)

  def valid_function(self):
    if self.op == "add":
      self.total += self.current
    if self.op == "soustr":
      self.total -= self.current
    if self.op == "multi":
      self.total *= self.current
    if self.op == "div":
      self.total /= self.current
    if self.op == "mod":
      self.total %= self.current     # ici "%" c'est le modulo
    self.input_valu = True
    self.check_sum = False
    self.display(self.total)

  def operation(self, op):
    self.current = float(self.current)
    if self.check_sum:
      self.valid_function()
    elif not self.result:
      self.total = self.current
      self.input_value = True
    self.check_sum = True
    self.op = op
    self.result = False

  def Clear_Entry(self):
    self.result = False
    self.current = "0"
    self.display(0)
    self.input_value = True

  def all_Clear_Entry(self):
    self.Clear_Entry()
    self.total = 0

  def mathsPM(self):
    self.result = False
    self.current = -(float(txtDisplay.get()))
    self.display(self.current)

  def squared(self):
    self.result = False
    self.current = math.sqrt(float(txtDisplay.get()))    # import math     ;-)
    self.display(self.current)    

  def cos(self):
    self.result = False
    self.current = math.cos(math.radians(float(txtDisplay.get())))
    self.display(self.current)

  def cosh(self):
    self.result = False
    self.current = math.cosh(math.radians(float(txtDisplay.get())))
    self.display(self.current)
    
  def tan(self):
    self.result = False
    self.current = math.tan(math.radians(float(txtDisplay.get())))
    self.display(self.current)

  def tanh(self):
    self.result = False
    self.current = math.tanh(math.radians(float(txtDisplay.get())))
    self.display(self.current)
    
  def sin(self):
    self.result = False
    self.current = math.sin(math.radians(float(txtDisplay.get())))
    self.display(self.current)

  def sinh(self):
    self.result = False
    self.current = math.sinh(math.radians(float(txtDisplay.get())))
    self.display(self.current)
    
  def log(self):   # logarithme
    self.result = False
    self.current = math.log(float(txtDisplay.get()))
    self.display(self.current)

  def exp(self):   # exposant
    self.result = False
    self.current = math.exp(float(txtDisplay.get()))
    self.display(self.current)
    
  def pi(self):     # le nombre Pi = 3.1415
    self.result = False
    self.current = math.pi
    self.display(self.current)

  def tau(self):    # "2π" = tau
    self.result = False
    self.current = math.tau
    self.display(self.current)
    
  def e(self):
    self.result = False
    self.current = math.e
    self.display(self.current)

  def acosh(self):
    self.result = False
    self.current = math.acosh(math.radians(float(txtDisplay.get())))
    self.display(self.current)

  def asinh(self):
    self.result = False
    self.current = math.asinh(math.radians(float(txtDisplay.get())))
    self.display(self.current)   
    
  def expm1(self):
    self.result = False
    self.current = math.expm1(float(txtDisplay.get()))
    self.display(self.current)

  def lgamma(self):
    self.result = False
    self.current = math.lgamma(float(txtDisplay.get()))
    self.display(self.current)

  def degrees(self):
    self.result = False
    self.current = math.degrees(float(txtDisplay.get()))
    self.display(self.current)

  def log2(self):
    self.result = False
    self.current = math.log2(float(txtDisplay.get()))
    self.display(self.current)

  def log10(self):
    self.result = False
    self.current = math.log10(float(txtDisplay.get()))
    self.display(self.current)

  def log1p(self):
    self.result = False
    self.current = math.log1p(float(txtDisplay.get()))
    self.display(self.current)


added_value = Calc()    # Nous l'exprimons comme ça pour changer, égaliser un mot à une fonction "Calc()"


#============= Création de l'afficheur ==============================================================

txtDisplay = Entry(calc, font=("arial",20,'bold'), background = "powder blue", bd = 30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")


#============= Créations des boutons grâce à row/ligne et column/colonnes via fonction range ========

numberpad = "789456123"
i = 0
btn = []     # définition de liste
for j in range(2,5):
  for k in range(3):
    btn.append(Button(calc, width=6, height = 2, font=("arial",20,'bold'),bd = 4, text= numberpad[i]))
    btn[i].grid(row = j, column = k, pady = 1)
    btn[i]["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)

    i += 1

#============= CALCULATRICE : =======================================================================

btnClear = Button(calc, text = chr(67), width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = added_value.Clear_Entry).grid(row=1, column=0, pady = 1)

btnAllClear = Button(calc, text = chr(67)+ chr(69), width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = added_value.all_Clear_Entry).grid(row=1, column=1, pady = 1)

# Racine Carrée :
btnCarre = Button(calc, text = "√", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = added_value.squared).grid(row=1, column=2, pady = 1)

# opérateurs :
btnAdd = Button(calc, text = "+", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = lambda: added_value.operation("add")).grid(row=1, column=3, pady = 1)

btnSoustr = Button(calc, text = "-", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = lambda: added_value.operation("soustr")).grid(row=2, column=3, pady = 1)

btnMult = Button(calc, text = "*", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = lambda: added_value.operation("multi")).grid(row=3, column=3, pady = 1)

btnDiv = Button(calc, text = chr(247), width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = lambda: added_value.operation("div")).grid(row=4, column=3, pady = 1)


# nombre 0 :
btnZero = Button(calc, text = "0", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady = 1)



btnPoint = Button(calc, text = ".", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady = 1)

btnPlusMoins = Button(calc, text = chr(177), width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = added_value.mathsPM).grid(row=5, column=2, pady = 1)

btnEgale = Button(calc, text = "=", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "powder blue",command = added_value.sum_of_total).grid(row=5, column=3, pady = 1)  


#============= CALCULATRICE SCIENTIFIQUE : ===========================================================

btnPi = Button(calc, text = "π", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "papaya whip",command = added_value.pi).grid(row=1, column=4, pady = 1)

btnCos = Button(calc, text = "cos", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "papaya whip",command = added_value.cos).grid(row=1, column=5, pady = 1)

btnTan = Button(calc, text = "tan", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "papaya whip",command = added_value.tan).grid(row=1, column=6, pady = 1)

btnSin = Button(calc, text = "sin", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "papaya whip",command = added_value.sin).grid(row=1, column=7, pady = 1)

#====================================================================================================

btn2Pi = Button(calc, text = "2π", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "cyan",command = added_value.tau).grid(row=2, column=4, pady = 1)

btnCosH = Button(calc, text = "cosh", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "cyan",command = added_value.cosh).grid(row=2, column=5, pady = 1)

btnTanH = Button(calc, text = "tanh", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "cyan",command = added_value.tanh).grid(row=2, column=6, pady = 1)

btnSinH = Button(calc, text = "sinh", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "cyan",command = added_value.sinh).grid(row=2, column=7, pady = 1)

#====================================================================================================

btnLog = Button(calc, text = "log", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "magenta",command = added_value.log).grid(row=3, column=4, pady = 1)

btnExp = Button(calc, text = "Exp", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "magenta",command = added_value.exp).grid(row=3, column=5, pady = 1)

btnMod = Button(calc, text = "Mod", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "magenta",command = lambda: added_value.operation("mod")).grid(row=3, column=6, pady = 1)  

btnE = Button(calc, text = "e", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "magenta",command = added_value.e).grid(row=3, column=7, pady = 1)

#====================================================================================================

btnLog2 = Button(calc, text = "log2", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "chartreuse",command = added_value.log2).grid(row=4, column=4, pady = 1)

btnDeg = Button(calc, text = "deg", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "chartreuse",command = added_value.degrees).grid(row=4, column=5, pady = 1)

btnACosH = Button(calc, text = "acosh", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "chartreuse",command = added_value.acosh).grid(row=4, column=6, pady = 1)  

btnASinH = Button(calc, text = "asinh", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "chartreuse",command = added_value.asinh).grid(row=4, column=7, pady = 1)  

#====================================================================================================

btnLog10 = Button(calc, text = "log10", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "yellow",command = added_value.log10).grid(row=5, column=4, pady = 1)

btnLog1p = Button(calc, text = "log1p", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "yellow",command = added_value.log1p).grid(row=5, column=5, pady = 1)

btnexpm1 = Button(calc, text = "expm1", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "yellow",command = added_value.expm1).grid(row=5, column=6, pady = 1)  

btnlgamma = Button(calc, text = "lgamma", width = 6, height = 2, font=("arial",20,'bold'),bd = 4,
                  background = "yellow",command = added_value.lgamma).grid(row=5, column=7, pady = 1)  

#================ INSCRIPTION sur la machine =======================================================

lblDisplay = Label(calc, text = "CALCULATRICE SCIENTIFIQUE", font=("arial",18,'bold'), justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)


#============= Fonctions pour les menus déroulants en haut de la fenêtre ===========================

def iExit():
  iExit = tkinter.messagebox.askyesno("Calculatrice Racine Carree", "Confirmez si vous voulez quitter")
  if iExit > 0:
    root.destroy()
    return

def Scientifique():
  root.resizable(width = False, height = False)
  root.geometry("944x568+0+0")
  
def Standart():
  root.resizable(width = False, height = False)
  root.geometry("480x568+0+0")


#============= Fonctionnalité déroulante en haut de la fenêtre ======================================

# ceci est le menu déroulant pour FILE :

menubar = Menu(calc)        # ------> nominations des fenêtres déroulantes

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Standard", command = Standart)
filemenu.add_command(label = "Scientific", command = Scientifique)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)


# ceci est le menu déroulant pour EDIT :

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")


# ceci est le menu déroulant pour HELP :

helpmenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "Vue Help")



root.config(menu = menubar)

root.mainloop()


# expérience "math" et "tkinter" et en partuiculier sur les menus déroulants en haut de la fenêtre
