from Davies import davies,checks
import tkinter
from lepion import lepion
from lepph import lepph
from Davies import davies,checks
from pqoextract import pqoextract
from shell import runshell
from pqigenetator import pqi

ph = [3,3.2,3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6,5.8,6.0,6.2,6.4,6.6,6.8,7.0,7.2,7.4,7.6,7.8,8.0,
          9.2,8.4,8.6,8.8,9.0,9.2,9.4,9.6,9.8,10.0]

ionic = [0.005,0.01,0.05,0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]


def isfloat(str):
    '''Function to check if the str is float.
    
    str text is the input.'''
    try:
        float(str)
        return True
    except ValueError:
        return False
def trydavies(metal,ligand):
      '''Function to check if the davies function works properly.
    
    metal and ligand comes from user input.'''
      try:
          checks(metal,ligand)
          return True
      except Exception():
          return False
      
def checkpqo(metal, ligand1, ligand2,ph1,ph2,ph3,ion1,ion2,ion3):
       '''Function to check if the pqo extract function work properly.
    
    metal and ligand comes from user input.'''
    
       try:
          pqoextract(metal, ligand1, ligand2,ph1,ph2,ph3,ion1,ion2,ion3)
          return True
       except:
           return False  

def checkshell():
       '''Function to check if the shell function work properly.
    
    metal and ligand comes from user input.'''
    
       try:
          runshell()
          return True
       except:
           return False 

  
def main(metal,ligand1,ligand2,ph1,ph2,ph3,ion1,ion2,ion3):
    '''Function to call each of the functions, to run the system intergreted.'''
    
    boos = False
    if checks(metal,ligand1) and checks(metal,ligand2):
     davies(metal, ligand1)
     davies(metal,ligand2)
     pqi(metal, ligand1)
     pqi(metal, ligand2)
     if checkshell():
      if checkpqo(metal, ligand1, ligand2,ph1,ph2,ph3,ion1,ion2,ion3):     
       lepion(metal,ligand1, ligand2)
       boos = lepph(metal, ligand1, ligand2)
      else:
        print("Not support"+metal+ ligand1+ligand2)
        tkinter.messagebox.showinfo(title='end', message= "Not support"+metal+ ligand1+ligand2)
        return False
      return boos
     else:
        tkinter.messagebox.showinfo(title='end', message= 'The shell cant run, maybe you are using windows')
        return False
    else:
        print("Not support"+metal+ ligand1+ligand2)
        tkinter.messagebox.showinfo(title='end', message= "Not support"+metal+ ligand1+ligand2)
        return False
    
def lepui():
    def daviess():
     check = False 
     if checkph1():
      if checkph2():
        if checkph3():
         if checkion1():
            if checkion2():
                if checkion3():
                     mental  = entrymental.get()
                     ligand1 = entryligand1.get()
                     ligand2 = entryligand2.get()
                     ph1 = entryph1.get()
                     ph2 = entryph2.get()
                     ph3 = entryph3.get()
                     ion1 = entryion1.get()
                     ion2 = entryion2.get()
                     ion3 = entryion3.get()
                     if ph1!=ph2 and ph2 !=ph3 and ph1!=ph3:
                         if ion1 != ion2 and ion2!=ion3 and ion1 != ion3:
                             if mental != "" and ligand1 != "" and ligand2 != "":
                                 check = True
                             else:
                                 tkinter.messagebox.showerror(title='end', message="Error, check the metal and ligand input")
                         else:
                           tkinter.messagebox.showerror(title='end', message="Error, check the ph and ion input")
                     else:
                             tkinter.messagebox.showerror(title='end', message="Error, check the ph and ion input")
     if check== True:
      
      if trydavies(mental,ligand1) and trydavies(mental,ligand2):
        if checks(mental,ligand1) and checks(mental,ligand2):
          if main(mental,ligand1,ligand2,ph1,ph2,ph3,ion1,ion2,ion3):
           tkinter.messagebox.showinfo(title='end', message='Done, LEP has been determined')
          else:
              tkinter.messagebox.showinfo(title='end', message='Done, No LEP determined')
          
        else:
          tkinter.messagebox.showerror(title='end', message="Error, can't find the metal or ligand, please check input")
        # main(mental,ligand1,ligand2)
      else:
        tkinter.messagebox.showerror(title='end', message="Error, can't find the metal or ligand, please check input")
     
    def cancel():
     varmental.set('')
     varligand1.set('')
     varligand2.set('')
    
    def checkph1():
        o = entryph1.get()
        if isfloat(o):
            if float(o) in ph:
                return True
            else:
             tkinter.messagebox.showinfo(title='end', message='Please enter correct ph1.')
        else:
            tkinter.messagebox.showinfo(title='end', message='Please enter correct ph1.')
            
    def checkph2():
        o = entryph2.get()
        
        if isfloat(o):
            if float(o) in ph:
                return True
            else:
               tkinter.messagebox.showinfo(title='end', message='Please enter correct ph2.')
        else:
            tkinter.messagebox.showinfo(title='end', message='Please enter correct ph2.')
            
    def checkph3():
        o = entryph3.get()
        
        if isfloat(o):
            if float(o)in ph:
                return True
            else:
              tkinter.messagebox.showinfo(title='end', message='Please enter correct ph3.')
        else:
            tkinter.messagebox.showinfo(title='end', message='Please enter correct ph3.')
            
    def checkion1():
        o = entryion1.get()
        
        if isfloat(o):
            if float(o) in ionic:
                return True
            else:
              tkinter.messagebox.showinfo(title='end', message='Please enter correct ion1.')
        else:
            tkinter.messagebox.showinfo(title='end', message='Please enter correct ion1.')
            
    def checkion2():
        o = entryion2.get()
        
        if isfloat(o):
            if float(o) in ionic:
                return True
            else:
              tkinter.messagebox.showinfo(title='end', message='Please enter correct ion2.')
        else:
            tkinter.messagebox.showinfo(title='end', message='Please enter correct ion2.')
    
    def checkion3():
        o = entryion3.get()
        
        if isfloat(o):
            if float(o) in ionic:
                return True
            else:
              tkinter.messagebox.showinfo(title='end', message='Please enter correct ion3.')
        else:
            tkinter.messagebox.showinfo(title='end', message='Please enter correct ion3.')
    
            
            
            
 
    window = tkinter.Tk()
    window.title('lep ui')
    window.geometry('700x350')
    varmental = tkinter.StringVar(value='')
    varligand1 = tkinter.StringVar(value='')
    varligand2 = tkinter.StringVar(value='')
    varph1 = tkinter.StringVar(value='')
    varph2 = tkinter.StringVar(value='')
    varph3 = tkinter.StringVar(value='')
    varion1 = tkinter.StringVar(value='')
    varion2 = tkinter.StringVar(value='')
    varion3 = tkinter.StringVar(value='')
    
    
    # Create the label for fuzzy search
    labelName = tkinter.Label(window, text='Metal', justify=tkinter.RIGHT, width=80)
    
    labelName.place(x=10, y=5, width=80, height=20)
    # Create the text box and the input text.
    entrymental = tkinter.Entry(window, width=80, textvariable=varmental)
    entrymental.place(x=100, y=5, width=80, height=20)
    
    labelPwd = tkinter.Label(window, text='ligand1', justify=tkinter.RIGHT, width=80)
    labelPwd.place(x=10, y=30, width=80, height=20)
    # Create the text box for the fuzzy number. 
    entryligand1 = tkinter.Entry(window,  width=80, textvariable=varligand1)
    entryligand1.place (x=100, y=30, width=80, height=20)
    
    labelName = tkinter.Label(window, text='ligand2', justify=tkinter.RIGHT, width=80)
    labelName.place(x=10, y=55, width=80, height=20)
    # Create the text box and the input text.
    entryligand2 = tkinter.Entry(window, width=80, textvariable=varligand2)
    entryligand2.place(x=100, y=55, width=80, height=20)
    
    labelName = tkinter.Label(window, text='ph1', justify=tkinter.RIGHT, width=80)
    labelName.place(x=10, y=80, width=80, height=20)
    # Create the text box and the input text.
    entryph1 = tkinter.Entry(window, width=80, textvariable=varph1)
    entryph1.place(x=100, y=80, width=80, height=20)
    
    labelName = tkinter.Label(window, text='ph2', justify=tkinter.RIGHT, width=80)
    labelName.place(x=200, y=80, width=80, height=20)
    # Create the text box and the input text.
    entryph2 = tkinter.Entry(window, width=80, textvariable=varph2)
    entryph2.place(x=290, y=80, width=80, height=20)
    
    labelName = tkinter.Label(window, text='ph3', justify=tkinter.RIGHT, width=80)
    labelName.place(x= 380, y=80, width=80, height=20)
    # Create the text box and the input text.
    entryph3 = tkinter.Entry(window, width=80, textvariable=varph3)
    entryph3.place(x=470, y=80, width=80, height=20)
    
    labelName = tkinter.Label(window, text='ion1', justify=tkinter.RIGHT, width=80)
    labelName.place(x=10, y=105, width=80, height=20)
    # Create the text box and the input text.
    entryion1 = tkinter.Entry(window, width=80, textvariable=varion1)
    entryion1.place(x=100, y=105, width=80, height=20)
    
    labelName = tkinter.Label(window, text='ion2', justify=tkinter.RIGHT, width=80)
    labelName.place(x=200, y=105, width=80, height=20)
    # Create the text box and the input text.
    entryion2 = tkinter.Entry(window, width=80, textvariable=varion2)
    entryion2.place(x=290, y=105, width=80, height=20)
    
    labelName = tkinter.Label(window, text='ion3', justify=tkinter.RIGHT, width=80)
    labelName.place(x= 380, y=105, width=80, height=20)
    # Create the text box and the input text.
    entryion3 = tkinter.Entry(window, width=80, textvariable=varion3)
    entryion3.place(x=470, y=105, width=80, height=20)
    

    
    
    
    # Create the buttons and the link related to them
    buttonOk = tkinter.Button(window, text='ok', command=daviess)
    buttonOk.place(x=10, y=180, width=100, height=20)
    buttonCancel = tkinter.Button(window, text='Cancel', command=cancel)
    buttonCancel.place(x=120, y=180, width=100, height=20)
    
    
    # Loop show the interface
    labelName = tkinter.Label(window, text='Input mental name Zn, Fe for example.', justify=tkinter.RIGHT, width=80)
    
    labelName.place(x=200, y=5, width=255, height=20)
    
    labelName = tkinter.Label(window, text='Input ligands name Citrate, Edta for example.', justify=tkinter.RIGHT, width=80)
    
    labelName.place(x=200, y=30, width=300, height=20)
    
    labelName = tkinter.Label(window, text='Input ligands name Citrate, Edta for example.', justify=tkinter.RIGHT, width=80)
    
    labelName.place(x=200, y=55, width=300, height=20)
    
    labelName = tkinter.Label(window, text='Ph can be chosen from follow list:[4 ,4.4 ,4.8 ,5.2 ,5.6 ,6 ,6.4 ,6.8 ,7.2 ,7.6 ,8 ,8.4 ,8.8 ,9.2 ,9.6 ,10]', justify=tkinter.RIGHT, width=80)
    
    labelName.place(x=0, y=130, width=670, height=20)
    
    labelName = tkinter.Label(window, text='ion can be chosen from follow list: [0.005,0.01,0.05,0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]', justify=tkinter.RIGHT, width=80)
    
    labelName.place(x=0, y=150, width=640, height=20)
    
    window .mainloop()

main("fe","citrate","edta",3,4,5,0.01,0.1,0.5)