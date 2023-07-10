

import os
dirlast = os.path.abspath('..')
template = dirlast+ '/template'+'/example.sh'
shell =  dirlast+ '/phreeqc/bin/shell.sh'
c1 = dirlast+ '/pqi'
c2 = dirlast+ '/pqi/'
c3 = dirlast+ '/pqo/'
# Command to run
c4 = "cd "+ dirlast+ "/phreeqc/bin && ./shell.sh"
# Command to give the addmission.
c5 = "cd "+ dirlast+ "/phreeqc/bin && chmod 777 shell.sh"
def runshell():
   '''Function to generate the shell script and run it.
    
   no required input'''
   f = open(template,'r')
   lines = f.readlines()
   outputs = open(shell, 'w')
   #Set the write bool , which can judge the programm to copy the template or make change of it.
   write = True
   #Begin to write the pqi files.
   for i in range(len(lines)):
    #When meet the part need to change, put our new text and stop copy the template.
    if 'oooo' in lines[i]:
        write = False
        new = lines[i].replace('oooo',c1)
        outputs.write(new)
    if 'for' in lines[i]:
        write = True
    if  'aaa'in lines[i]:
        write = False
        new = lines[i].replace('aaa',c2)
        outputs.write(new)
    if  'bbb'in lines[i]:
        write = False
        new = lines[i].replace('bbb',c3)
        outputs.write(new)
    if '.pqi.out' in lines[i]:
        write = True
    
     # If write is true, continue copy from the template.
    if write == True:
            outputs.write(lines[i])
   outputs.close() 
  
   os.system(c5)       
   os.system(c4)  

runshell()