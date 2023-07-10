import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
import os

def lepph(metal,ligand1,ligand2):
    '''generates the lep plot for pH using the csv file generated from the extract function
    
    The metal and two ligands comes from user input.'''
    print("Begin draw lep:")
    print("/n")
    dirlast = os.path.abspath('..')
    table = dirlast+'/lepcsv/'+metal+"_"+ligand1+"_"+ligand2+"_"+"ph"+'.csv' 
    df = pd.read_csv(table)
    fraction = []
    name = []
    cur =[]
    w = []
    namee = ""

    namee = str(df.iloc[1,1]) + "_"+str(df.iloc[0,1])
     #Get the fraction from the csv files.
    for i in range(6):
     cur = []

     name.append(str(df.iloc[i,0])+df.iloc[i,1])
   
     for j in range(2,38):
  
        cur.append(float(df.iloc[i,j]))
        
     fraction.append(cur)
    
    ph = [3,3.2,3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6,5.8,6.0,6.2,6.4,6.6,6.8,7.0,7.2,7.4,7.6,7.8,8.0,
          8.2,8.4,8.6,8.8,9.0,9.2,9.4,9.6,9.8,10.0]
    colors = ['r','r','c','c','b','b','y','y']
    c = ['ro','ro','co','co','bo','bo','yo','yo']
    lss = ['--','-','--','-','--','-','--','-']
     #Begin to plot the LEP diagram
    for i in range(len(fraction)):
       #Draw the two lines in the diagrams.
      plt.plot(ph,fraction[i] ,ls=lss[i],color=colors[i],marker =",", lw=1,label=name[i])
        
      cur = 0
      mins = 10000
      loc = -1
      #Begin to find the closest point within the csv data, as it should be a pair to find, we only do when i%2 == 1.
      if i%2 == 1:
          for j in range(len(fraction[0])):
               cur = abs(fraction[i-1][j]-fraction[i][j])
               if cur<mins and fraction[i-1][j]<0.9 and fraction[i-1][j]>0.02 and fraction[i][j]<0.9 and fraction[i][j]>0.02:
                   mins = cur
                   loc = j
           #Get the point to be infinitely close
          if loc !=-1 and loc !=0 and loc != len(fraction[0])-1:
           #Split the interval into 10000 small points.
           x3 = np.linspace(ph[loc], ph[loc+1], 10000)       
           y1_new = np.linspace(fraction[i-1][loc], fraction[i-1][loc+1], 10000) 
           y2_new = np.linspace(fraction[i][loc], fraction[i][loc+1], 10000) 
            #Get the two point that the two points close to the minal value we set
           idx = np.argwhere(np.isclose(y1_new, y2_new, atol=1e-04)).reshape(-1)
           if idx.any():
            #If we found the point we plot them.
            plt.plot(x3[idx], y2_new[idx], c[i])
           else:
            x3 = np.linspace(ph[loc-1], ph[loc], 10000)      
            y1_new = np.linspace(fraction[i-1][loc-1], fraction[i-1][loc], 10000) 
            y2_new = np.linspace(fraction[i][loc-1], fraction[i][loc], 10000) 
            idx = np.argwhere(np.isclose(y1_new, y2_new, atol=1e-04)).reshape(-1)
            plt.plot(x3[idx], y2_new[idx], c[i])
           if x3[idx] and y2_new[idx]:
            w.append([df.iloc[i,0],round(max(x3[idx]),3), round(max(y2_new[idx]),3)])
         
          
        
    plt.xlabel('ph')
    plt.ylabel('fraction of complexed Zinc')
    
    plt.legend()
    plt.savefig(dirlast+ '/lepfig/'+namee+metal+"_"+'_ph.jpg',bbox_inches='tight')
    
    outputs = open(dirlast+ '/lepout/'+namee+'_ph.txt', 'w')
    for i in range(len(w)):
      outputs.write("ionic strength:"+str(w[i][0]))
      outputs.write("\n")
      outputs.write("ph:"+str(w[i][1]))
      outputs.write("\n")
      outputs.write("Fraction:"+str(w[i][2]))
      outputs.write("\n")
      outputs.write("---------------------------------")
      outputs.write("\n")
    outputs.close()
    print(w)
    if w:
        print("we found the lep")
        return True
    else:
        print("No lep founded ")
        return False


lepph("Zn","Citrate","Edta")