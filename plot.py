

import os
import matplotlib.pyplot as plt
import tkinter
import tkinter.messagebox
import pandas as pd

ML = "FeCitrate"
dirlast = os.path.abspath('..')
table =dirlast+ '/davies'+'/FeCitrate'+ '.csv' 
table =dirlast+ '/davies'+'/'+ ML + '.csv' 
df = pd.read_csv(table)
name = []
ionic = [0.05,0.15,0.3,0.5,0.6]
logb= []
for i in range(0,3):
    r = df.iloc[i,0]
    equal = r.find("=")
    names = r[equal+2:len(r)].strip("\n")
    name.append(names)
    logbs = []
    for j in range(2,7):
       logbs.append(df.iloc[i,j])
    logb.append(logbs)
colors = ['r','y','c','g','b','k','r','y','c','g','b','k']
a = ""
for i in range(len(logb)):
 plt.plot(ionic,logb[i] , ls="-",color=colors[i],marker =",", lw=2, label=name[i])
 a = name[i]+"_"+ a
plt.xlabel('Ionic Strength')
plt.ylabel('LogB')
plt.legend()
plt.savefig(dirlast+ '/daviesfig/'+a+'.jpg',bbox_inches='tight')
plt.show()

print(name)
print(logb)
