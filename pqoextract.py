import os
from pandas.core.frame import DataFrame

def find(s,ligand1):
    '''Find the concentration from the target lines include the complexes.
    The s-line and ligand comes from pqoextract function.'''
    starts = 0
    ends = 0
    c = False
    b = False
    for m in range(s.find(ligand1),len(s)):
                  if s[m] == " ": 
                      c = True
                  if s[m] != " " and c ==True:
                      starts = m
                      b = True
                      c = False
            
                  if s[m]==" " and b ==True:
                      ends = m
                      break
    return starts,ends 
    
def pqoextract(metal,ligand1,ligand2,ph1,ph2,ph3,ion1,ion2,ion3):
    '''Extract the concentration from the pqo files and output three csv files.
    
    The metal ligand and ph ionic strength comes from user input'''
    print("Begin pqoextract operation:")
    print("/n")
    ph = [3,3.2,3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0,5.2,5.4,5.6,5.8,6.0,6.2,6.4,6.6,6.8,7.0,7.2,7.4,7.6,7.8,8.0,
          8.2,8.4,8.6,8.8,9.0,9.2,9.4,9.6,9.8,10.0]
    
    p = ph.index(float(ph1))
    pp = ph.index(float(ph2))
    ppp = ph.index(float(ph3))
    ionic = [ion1 , ion2 , ion3]
    metal_conc = 2.000e-04
    total = []
    dirlast = os.path.abspath('..')
    name = []
    ions= []
    total2 =[]
    name2 = []
    ions2 = []
    totalph = []
    phs = []
    fractionph = []
    for ion in range(len(ionic)):
     fraction = []
     fractionph = []
     path1 = dirlast + "/pqo/"+str(ionic[ion])+metal+ligand1+".pqi.pqi.out"
     path2 = dirlast+ "/pqo/"+str(ionic[ion])+metal+ligand2+".pqi.pqi.out"
     
     #Open the pqi files.
     f = open(path1,'r', encoding='gb18030',errors='ignore')
     
     lines = f.readlines()
     start = []
     end = []
     fraction = []
     fractionph = []
      # finds the part that include the information on the fraction of complexes in the pqo files. 
     for i in range(len(lines)):
        if "Distribution of species" in lines[i]:
            start.append(i)
        if "Saturation indices" in lines[i]:
            end.append(i)
     # Begin extract the concentrations,
     for i in range(len(start)):
        tph = 0
        for s in lines[start[i]:end[i]]:
            if metal in s and ligand1 in s:   
                starts,ends = find(s,ligand1)
                tph = tph+float(s[starts:ends].strip())
        tph = tph/2        
        fraction.append(round(tph/metal_conc,3)) 
         # Set the limitation for the output ph csv.
        if i == p or i == pp or i ==ppp:
           fractionph.append(round(tph/metal_conc,3)) 
     name.append(ligand1)
     total.append(fraction)
     ions.append(ionic[ion])
      # Set the limitation for the output ion csv.
     if ionic[ion]==float(ion1) or ionic[ion]==float(ion2) or ionic[ion] == float(ion3):
         name2.append(ligand1)
         total2.append(fraction)
         ions2.append(ionic[ion])
     f = open(path2,'r', encoding='gb18030',errors='ignore')
     # Save the dataset this search result from 
     lines = f.readlines()
     start = []
     end = []
     fraction = []
     
     for i in range(len(lines)):
        if "Distribution of species" in lines[i]:
            start.append(i)
        if "Saturation indices" in lines[i]:
            end.append(i)
    
     for i in range(len(start)):
        tph = 0
        for s in lines[start[i]:end[i]]:
            if metal in s and ligand2 in s:
                starts,ends = find(s,ligand2)
                tph = tph+float(s[starts:ends].strip())    
        tph = tph/2        
        fraction.append(round(tph/metal_conc,3))
        if i == p or i == pp or i ==ppp:
           
           fractionph.append(round(tph/metal_conc,3)) 
     f = []
     for i in range(3):
         f.append(fractionph[i])
         f.append(fractionph[i+3])
     totalph.append(f)
     name.append(ligand2)
     total.append(fraction)
     ions.append(ionic[ion])
     
     if ionic[ion]==float(ion1) or ionic[ion]==float(ion2) or ionic[ion] == float(ion3):
         print("0")
        
         name2.append(ligand2)
         total2.append(fraction)
         ions2.append(ionic[ion])
  
    
    phs = [ph1,ph1,ph2,ph2,ph3,ph3]
    totalphnew = []
    s = []
    w = []
    e = []
    ss = []
    ww =[]
    ee =[]
    print(total2)
     # Set the format of the ph files.
    for i in range(len(totalph)):
        s.append(totalph[i][-2])
        ss.append(totalph[i][-1])
        w.append(totalph[i][-4])
        ww.append(totalph[i][-3])
        e.append(totalph[i][-6])
        ee.append(totalph[i][-5])
    totalphnew.append(e)
    totalphnew.append(ee)
    totalphnew.append(w)
    totalphnew.append(ww)
    totalphnew.append(s)
    totalphnew.append(ss)
    phtabel = dirlast+'/lepcsv/'+metal+"_"+ligand1+"_"+ligand2+"_"+"ph"+'.csv' 
    iontabel =   dirlast+'/lepcsv/'+metal+"_"+ligand1+"_"+ligand2+"_"+"ion"+'.csv'
    alltabel = dirlast+'/lepcsv/'+metal+"_"+ligand1+"_"+ligand2+"_""all"+'.csv' 
    data = {"ionic":ions,"name":name}
    for i in range(len(ph)):
           data[str(ph[i])] = [t[i] for t in total]
  
    dataframe=DataFrame(data)
  
    dataframe.to_csv(alltabel,index=False,sep=',')
    
    datas = {"ionic":ions2,"name":name2}
    for i in range(len(ph)):
            datas[str(ph[i])] = [t[i] for t in total2]
    
    dataframe=DataFrame(datas)
 
    dataframe.to_csv(phtabel,index=False,sep=',')
    
    datass = {"ph":phs,"name":name2}
    for i in range(len(ionic)):
            datass[str(ionic[i])] = [t[i] for t in totalphnew]
    
    dataframe=DataFrame(datass)

    dataframe.to_csv(iontabel,index=False,sep=',')
     
pqoextract('Zn','Citrate','Edta',3,5,7,0.01,0.2,0.3) #user should change the metal ligand, Ph ranges and ionic strength , must have pqo files of this in the PQO folder