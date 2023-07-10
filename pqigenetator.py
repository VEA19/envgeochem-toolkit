
import os
import matplotlib.pyplot as plt
import tkinter
import tkinter.messagebox
import pandas as pd

ionic_list = [0.5,0.6,0.7] #specify the modelling ionic strength 

def pqi(metal,ligand,ionic_list): #Generates a PQI for PHREEQC processing
    dirlast = os.path.abspath('..')
    table =dirlast+ '/davies'+'/'+metal+ligand+ '.csv'
    template = dirlast+ '/template'+'/example'+ '.pqi'
    df = pd.read_csv(table)
    name = []
    logb= []
    #Get the new logb on full dataset of ionic strength.
    for i in range(len(df['Reaction'])):
        r = df.iloc[i,0].strip('\n')
        name.append(r)
        logbs = []
        for j in range(2,15):
           logbs.append(df.iloc[i,j])
        logb.append(logbs)
    print(logb)
    print(name)
    print(len(df['Reaction']))
    # Generate pqi files in turn.
    for ion in range(len(ionic_list)):
      #Set the generate files' path.
     pqi =dirlast+ '/pqi'+'/'+ str(ionic_list[ion])+metal+ ligand+ '.pqi' 
     f = open(template,'r')
     lines = f.readlines()
     outputs = open(pqi, 'w')
      #Set the write bool , which can judge the programm to copy the template or make change of it.
     write = True
     #begin writing the PQI file
     outputs.write("DATABASE "+ dirlast+"/phreeqc/database/minteq.v4.dat")
     outputs.write("\n")
     for i in range(1,len(lines)):
           if 'SOLUTION_MASTER_SPECIES' in lines[i]:
               outputs.write("SOLUTION_MASTER_SPECIES")
               outputs.write("\n")
               write = False 
               master = master =dirlast+ '/davies'+'/'+ 'MASTER_SPECIES' + metal +ligand +'.txt'
               f = open(master,'r')
               liness = f.readlines()
               for l in liness:
                outputs.write(l)
               outputs.write("END")
               outputs.write("\n")
               outputs.write("   ")
               outputs.write("\n")
               outputs.write("SOLUTION_SPECIES")
               outputs.write("\n")
               for m in range(len(name)):
                   outputs.write(name[m])
                   outputs.write("\n")
                   outputs.write("log_k		"+str(logb[m][ion]))
                   outputs.write("\n")
               outputs.write("END")
               outputs.write("\n")
               outputs.write("   ")
               outputs.write("\n")
           # Define the part we need to update is over, set the write to ture, continue to copy the template.
           if 'SOLUTION ' in lines[i]:
               write = True
           if 'Zns' in lines[i]:
               write = False
               new = lines[i].replace('Zns',metal)
               outputs.write(new)
               new2 = lines[i+1].replace('Citrates',ligand)
               outputs.write(new2)
               outputs.write("END")
               outputs.write("\n")
               outputs.write("\n")
           if 'Cl' in lines[i]:
               write = False
               new = lines[i].replace('0.1',str(ionic_list[ion]))
               outputs.write(new)
           if 'Na' in lines[i]:
               write = False
               new = lines[i].replace('0.1',str(ionic_list[ion]))
               outputs.write(new)
    
              
            # If write is true, continue copy from the template.
           if write == True:
            outputs.write(lines[i])
     outputs.close() 


pqi('Zn','citrate',ionic_list)