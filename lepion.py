
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
import os
def lepion(metal,ligand1,ligand2,ion1,ion2,ion3):
    '''generates the lep plot for ionic strength using the csv file generated from the extract function
    
    The metal and two ligands comes from user input.'''
    dirlast = os.path.abspath('..')
    table =dirlast+'/lepcsv/'+metal+"_"+ligand1+"_"+ligand2+"_""ion"+'.csv' 
    df = pd.read_csv(table)
    fraction = []
    name = []
    cur =[]
    w = []
    namee = ""
    namee = str(df.iloc[1,1]).strip("\xa0") + "_"+str(df.iloc[0,1]).strip("\xa0")
    #Get the fractioon from the csv files.
    for i in range(6):
     cur = []
     name.append(str(df.iloc[i,0])+df.iloc[i,1].strip("\xa0"))
     for j in range(2,5):
        cur.append(float(df.iloc[i,j]))
     fraction.append(cur)
    ionic = [ion1,ion2,ion3]
    colors = ['r','r','c','c','b','b','y','y']
    c = ['ro','ro','co','co','bo','bo','yo','yo']
    lss = ['--','-','--','-','--','-','--','-']
    a = ""
    print(fraction)
    #Begin to plot the LEP diagram
    for i in range(len(fraction)):
      plt.plot(ionic,fraction[i] ,ls=lss[i],color=colors[i],marker =",", lw=1,label=name[i])
       
      cur = 0
      mins = 10000
      loc = -1
      #Begin to find the closest point within the csv data, as it should be a pair to find, we only do when i%2 == 1.
      if i%2 == 1:
            for j in range(len(fraction[0])):
                 cur = abs(fraction[i-1][j]-fraction[i][j])
                 # Set the limitation as we have to find the exchange point. Not the point both two near smallest or biggest.
                 if cur<mins and fraction[i-1][j]<0.9 and fraction[i-1][j]>0.02 and fraction[i][j]<0.9 and fraction[i][j]>0.02:
                     mins = cur
                     loc = j
            #Get the point to be infinitely close
            if loc !=-1 and loc !=0 and loc != len(fraction[0])-1:
            #Split the interval into 10000 small points.
             x3 = np.linspace(ionic[loc], ionic[loc+1], 10000)       
             y1_new = np.linspace(fraction[i-1][loc], fraction[i-1][loc+1], 10000) 
             y2_new = np.linspace(fraction[i][loc], fraction[i][loc+1], 10000) 
              #Get the two point that the two points close to the minal value we set
             idx = np.argwhere(np.isclose(y1_new, y2_new, atol=0.0001)).reshape(-1)
              #If we found the point we plot them.
             if idx.any():
              plt.plot(x3[idx], y2_new[idx], c[i])
             else:
              x3 = np.linspace(ionic[loc-1], ionic[loc], 10000)       
              y1_new = np.linspace(fraction[i-1][loc-1], fraction[i-1][loc], 10000) 
              y2_new = np.linspace(fraction[i][loc-1], fraction[i][loc], 10000) 
              idx = np.argwhere(np.isclose(y1_new, y2_new, atol=0.0001)).reshape(-1)
              plt.plot(x3[idx], y2_new[idx], c[i])
             if x3[idx] and y2_new[idx]:
              w.append([df.iloc[i,0],round(max(x3[idx]),3), round(max(y2_new[idx]),3)])
           
          # plt.plot(ph[loc] , y  ,'ro')  
     
    plt.xlabel('ionic')
    plt.ylabel('fraction of complexed Zinc')
    plt.legend()
    plt.savefig(dirlast+ '/lepfig/'+metal+"_"+namee+'_ion.jpg',bbox_inches='tight')
    
    outputs = open(dirlast+ '/lepout/'+namee+'_ion.txt', 'w')
    
    for i in range(len(w)):
      outputs.write("ph:"+str(w[i][0]))
      outputs.write("\n")
      outputs.write("ion:"+str(w[i][1]))
      outputs.write("\n")
      outputs.write("Fraction:"+str(w[i][2]))
      outputs.write("\n")
      outputs.write("---------------------------------")
      outputs.write("\n")
    outputs.close()

lepion('Zn','Citrate','EDTA', 0.01 , 0.2 , 0.3)  #specify the metal + ligand and ionic strengths 