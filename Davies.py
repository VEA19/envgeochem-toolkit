import re
import math
import os
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import tkinter
import tkinter.messagebox
import pandas as pd
#Set the work dir
dirlast = os.path.abspath('..')

#The method to get all filename under the filepath
def readDir(dirPath):
    '''The fix search method to return the fix search result.
    
    search text comes from user input.'''
    allFiles = []
    if os.path.isdir(dirPath):
        fileList = os.listdir(dirPath)
        for f in fileList:
            if(f!="extraction" and f!=".DS_Store"):    
             f = dirPath+'/'+f
             allFiles.append(f)
    return allFiles 

#Function to check if the str is float.
def isfloat(str):
    '''Function to check if the str is float.
    
    str text is the input.'''
    try:
        float(str)
        return True
    except ValueError:
        return False
    
#Function to check if the metal and ligand can be found from the databse   
def checks(metal,ligand,database):
    '''Function to check if the metal and ligand can be found from the databse 
    
    metal and ligand comes from the user input.'''
    print("Begin davies check operation:")
    print("/n")
    logk = []
    reaction = []
    datafrom = []
    file = dirlast+ '/data'+'/'+database + '.txt' #change the path name (Add this to code function)
    f = open(file,'r')
    #Get the dataset the data from.
    dataset = file[file.find("data")+5:50].strip(".txt")
    check = 0
    check2 = 0
    lines = f.readlines()

    for i in range(len(lines)):
          if check ==0:
              if metal in lines[i]:
                   check = 2
          if check2 ==0:
              if ligand in lines[i]:
                   check2 = 3
          if metal in lines[i]:
             if ligand in lines[i]:
             # if "E" in lines[i]:
              if "log_k"in lines[i+1]:
               react = lines[i]
               reaction.append(react)
               k = lines[i+1][lines[i+1].find("k")+1:20].strip()
               logk.append(float(k))
               datafrom.append(dataset)
    if not reaction:
        return False
    else:
        return True
        print("present in database")
   
      
def davies(metal,ligand,database):#works for any database with the same format to minteqv4
    ''' Davies function to extract the metal and ligands from the database and perform the davies operation to calculate the logb. 
    
    metal and ligand comes from the user input.'''
    print("Begin davies operation:")
    print("/n")
    #Set the list used to store the paramate we used for the caculate.
    logk = []
    reaction = []
    datafrom = []
    ztotal = []
    vtotal = []
    ionic = [0.005,0.01,0.05,0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    file = dirlast+ '/data'+'/'+database + '.txt' 
    print(file)
    f = open(file,'r')
    dataset = file[file.find("data")+5:50000].strip(".txt")
    check = 0
    check2 = 0
    lines = f.readlines()
    # Store the master species information from the database used to generate the pqi files.
    master =dirlast+ '/davies'+'/'+ 'MASTER_SPECIES' + metal +ligand +'.txt'
    outputs = open(master, 'w')
    # Begin to check if the search metal and ligands in the database lines.
    for i in range(len(lines)):
          if check ==0:
              if metal in lines[i]:
                   outputs.write(lines[i])
                   check = 2
          if check2 ==0:
              if ligand in lines[i]:
                   outputs.write(lines[i])
                   check2 = 3
          if metal in lines[i]:
             if ligand in lines[i]:
             # if "E" in lines[i]:
              if "log_k"in lines[i+1]:
               react = lines[i]
               reaction.append(react)
               #Store the logk.
               k = lines[i+1][lines[i+1].find("k")+1:20].strip()
               logk.append(float(k))
               datafrom.append(dataset)
    if not reaction:
        return False
    outputs.close()
    k = 0 
    txt = dirlast+ '/davies'+'/'+metal+ligand+ '.txt'  
    output = open(txt, 'w') 
    tabel =dirlast+ '/davies'+'/'+ metal + ligand + '.csv' 
    validate = dirlast+ '/validate'+'/'+  metal + ligand + '.csv'
    names = []
    # Begin the davies operations.
    for r in reaction:
     z = []
     v = []
     r = r.strip()
     log_k = logk[k]
     output.write(r)
     output.write("\n")
     output.write("----------------------------------------------------")
     output.write("\n")
     output.write("logk: " + str(log_k))
     print(log_k)
     output.write("\n")
     output.write("Find from: "+datafrom[k])
     output.write("\n")
     output.write("\n")
     output.write("----------------------------------------------------")
     output.write("\n")
     symbol = []
     num = []
     k = k+1
    
     # 0 is on the left, 1 is on the right
     position = []
     amount = []
     logb = []              
     #Find all index of space
     elements = [each.start() for each in re.finditer(" ", r)]  
     
     number = int((len(elements)-2)/2+2)
     
     equal = r.find("=")
     name = r[equal+2:len(r)]
     names.append(name)
     
     
     # Do operation to the first elements eg. Zn+2 + 2Citrate-3 = Zn(Citrate)2-4
     # Judge the first character if or not a digit
     if r[0].isdigit():
        amount.append(float(r[0]))
     else:
        amount.append(1.00)
     # Judge the last character of first elements, which is 2 in this exp, if or not a digit
     if r[elements[0]-1:elements[0]].isdigit():
      num.append(float(r[elements[0]-1:elements[0]]))
      # To find the +,- of the elements, do loop to check each character in Zn+2 if 
     #  or not a letter in this exp.
      for i in range(0,elements[0]-1):   
       if not r[i].isalnum():
        if r[i] != " ":
          symbol.append(r[i])
     # if the last character of first elements, is +, - ,the num is 1.
     elif r[elements[0]-1:elements[0]]=="+" or r[elements[0]-1:elements[0]]=="-" :
        symbol.append("NA")
        num.append(1.00)
      # else the num is 0
     else:
        num.append(0.00)
        symbol.append(r[elements[0]-1:elements[0]])
    
     position.append(0)
     
     for i in range(number):
       # Do operation to the  elements between first and last
       if i !=0 and i != number-1:
        #  locate the location of them, same as before
        if r[elements[i*2]-1:elements[i*2]].isdigit():
         num.append(float(r[elements[i*2]-1:elements[i*2]]))
         for j in range(elements[(i-1)*2+1],elements[i*2]-1):
             if not r[j].isalnum():
                 if r[j] != " ":
                  symbol.append(r[j])
        elif r[elements[i*2]-1:elements[i*2]]=="+" or r[elements[i*2]-1:elements[i*2]]=="-":
         symbol.append("NA")
         num.append(1.00)
        else:
             num.append(0.00)
             symbol.append(r[elements[i*2]-1:elements[i*2]])  
        # Juge it's position by compare with the " = "
        if elements[i*2]-1 < equal:
            position.append(0)
        else:
            position.append(1.00)
    
        if r[elements[i*2-1]+1:elements[i*2-1]+2].isdigit():
         
         amount.append(float(r[elements[i*2-1]+1:elements[i*2-1]+2]))
        else:
         amount.append(1.00)
    # Do operation to the last one
     if r[len(r)-1:len(r)].isdigit():
      num.append(float(r[len(r)-1:len(r)]))
      for i in range(elements[len(elements)-1],len(r)):   
       if not r[i].isalnum():
        if r[i] != " ":
          symbol.append(r[i])
     elif r[len(r)-1:len(r)]=="+" or r[len(r)-1:len(r)]=="-":
         symbol.append("NA")
         num.append(1.00)
         
     else:
        num.append(0.00)
        symbol.append(r[len(r)-1:len(r)])
     position.append(1.00) 
    
     if r[elements[len(elements)-1]+1].isdigit():
        amount.append(float(r[elements[len(elements)-1]+1]))
     else:
        amount.append(1.00)
              
     cals1 = 0.0
     cals2 = 0.0
     cals3 = 0.0
     print(r)
     print(num)
     print(amount)
     print(r[len(r)-1:len(r)])
     
     coe = []
    # Do caculation to the full ionic dataset.
     for ion in ionic:
      cal = []
      coefcient = 0.00
      for i in range(len(position)):
            cals1 = -0.51*num[i]*num[i]
            cals2 =math.sqrt(ion)/(1+math.sqrt(ion)) - 0.3 * ion
            cals3 = cals1*cals2*amount[i]
            if position[i]==1:
                cals3 = -cals3
            cal.append(cals3)
      for c in cal:
        coefcient = coefcient +c
      coe.append(coefcient) 
      
    #Add the coeffcient to the logk to get the logb at different ionic strength.
     for co in coe:
        logB = co+log_k 
        logb.append(round(logB,3))
     plot = logb
     io = [0.005,0.01,0.05,0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
     plt.plot(io, plot, ls="-",color="r",marker =",", lw=2, label=r)
     plt.xlabel('Ionic Strength')
     plt.ylabel('LogB')
     plt.legend()
     plt.savefig(dirlast+ '/daviesfig/'+name.strip()+'.jpg',bbox_inches='tight')
     for i in range(len(ionic)):
         z.append(logb[i])
     for i in range(len(ionic)):
         v.append(-coe[i])
     ztotal.append(z)
     vtotal.append(v)
     for i in range(len(ionic)):
        print("ionic " + str(ionic[i])+"= " + str(coe[i])) 
        print("logb when ionic " + str(ionic[i])+"= " + str(logb[i]))
       
        output.write("ionic " + str(ionic[i])+"=" + str(logb[i]).encode("utf-8").decode("utf-8"))
        output.write("\n")
        
     output.write("----------------------------------------------------")    
     output.write("\n")
    output.close()
    #Build the data dictionary.
    data = {"Reaction":reaction,"logk":logk}
    # Add key and vaue to the data dic according to how many ionic strength we have.
    for i in range(len(ionic)):
     data[str(ionic[i])] = [t[i] for t in ztotal]
    dataframe=DataFrame(data)
    dataframe.to_csv(tabel,index=False,sep=',')
   
    
    #Build the dic for the validate files, which only include the activity coeffcient for the validation.
    datas = {"species":names,"logk":logk}
    for i in range(len(ionic)):
     datas[str(ionic[i])] = [t[i] for t in vtotal]
    dataframe=DataFrame(datas)
    dataframe.to_csv(validate,index=False,sep=',')
    fileList = os.listdir(dirlast+ '/davies')
    #If nothing generate, means no reactions found in database, return false to tell user.
    for fl in fileList:
     if os.path.getsize(dirlast+ '/davies/'+fl) == 0:
                os.remove(dirlast+ '/davies/'+fl)
                return False
    return True


checks("Zn","Citrate","ricesoil") #Case sentitive , have captials for metal and ligand
davies("Zn","Citrate","ricesoil")




