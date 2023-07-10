
import os
from pandas.core.frame import DataFrame
import tkinter
import tkinter.messagebox
from fuzzywuzzy import process
# Get the files' path
dirlast = os.path.abspath('..')
def readDir(dirPath):
    '''Get all file name under the dirpath
    
    dirpath come from the requirements.'''
    allFiles = []
     #Loop to get all file names.
    if os.path.isdir(dirPath):
        fileList = os.listdir(dirPath)
        for f in fileList:
            if(f!="extraction" and f!=".DS_Store"):    
             f = dirPath+'/'+f
             allFiles.append(f)
    return allFiles 

# fix search Extract
def extract(text):
  '''The fix search method to return the fix search result.
    
    search text comes from user input.'''
  # The path of the output files.
  txt = dirlast+ '/output'+'/'+text + '.txt'
  table =dirlast+ '/table'+'/'+ text + '.csv'
  output = open(txt, 'w')
  logk = []
  reaction = []
  datafrom = []
  #Read files 
  for file in readDir(dirlast+"/data"):
    f = open(file,'r')
    # Save the dataset this search result from 
    dataset = file[file.find("data")+5:5000].strip(".txt")
    check = 0
    lines = f.readlines()
    linenumber = 0
    # Begin the search
    for i in range(len(lines)-2):
      # First ensure the search text is in this line, and then ensure it is a reaction by "="
      if text in lines[i] and  "=" in lines[i]:
          # There is two format of logk, neighboor and two lines behind the last one.
          if "log_k"in lines[i+1]:
           linenumber = i+1
          if "log_k"in lines[i+2]:
           linenumber = i+2
          # Extract logK according to the different situation
          if "log_k"in lines[i+1] or "log_k"in lines[i+2]:
          # Get the reaction
           react = lines[i].strip().strip('#').strip()
           reaction.append(react)
           # Get logk
           k = lines[linenumber][lines[linenumber].find("k")+1:50].strip()
           # only save the logk when k not euaql to  0
           if k != 0:
            logk.append(k)
            datafrom.append(dataset)
            # Write the output file.
            if check == 0:
                output.write("\n")
                output.write("----------------------------------------------------")
                output.write("\n")
                output.write("Find from: "+dataset )
                output.write("\n")
                output.write("----------------------------------------------------")
                output.write("\n")
                check = check+1
            output.write("\n")
            output.write("\n")
            output.write(lines[i].strip().strip('#').strip())
            output.write("\n")
            output.write(lines[linenumber].strip().strip('#').strip())
            # Save the data into dataframe 
            data = {"Reaction":reaction,"logk":logk,"database":datafrom}
            dataframe=DataFrame(data)
            # Save the dataframe to the csv file.
            dataframe.to_csv(table,index=False,sep=',')
  output.close()
  fileList = os.listdir(dirlast+ '/output')
  for fl in fileList:
     if os.path.getsize(dirlast+ '/output/'+fl) == 0:
                os.remove(dirlast+ '/output/'+fl)
                return False
  return True


def fuzzyextract(text,number = 100):
  '''The fuuzy search method to return the fuzzy search result.
    
    search text and numbers comes from user input.'''
  # The path of the output files.
  table =dirlast+ '/table'+'/'+ text + '.csv'
  # List conclude all logk value.
  logk = []
  # List conclude all reaction text.
  reaction = []
  # List conclude all dataset the reaction from.
  datafrom = []
  logknew = []
  reactionnew = []
  datafromnew = []
  name = []
  namenew = []
  
  for file in readDir(dirlast+"/data"):
    f = open(file,'r',encoding='utf-8')
    dataset = file[file.find("data")+5:50000].strip(".txt")
    check = 0
    ks = 0.02
    lines = f.readlines()
    checkifexist = False
    linenumber = 0
    for i in range(len(lines)-2):
      checks = False
      # Save all the reactions
      if  "=" in lines[i]:
         # if "E" in lines[i]:
          if "log_k"in lines[i+1]:
           linenumber = i+1
           checks = True
          if "log_k"in lines[i+2]:
           linenumber = i+2
           checks = True
          ks = lines[linenumber][lines[linenumber].find("k")+1:50].strip()
          
          if "#" in ks:
               ks = ks[0: ks.find("#")-2]
          if checks==True:
           
           react = lines[i].strip().strip('#').strip()
           named = lines[i-1].strip()
           reaction.append(react)
           name.append(named)
           k = ks
           logk.append(k)
           datafrom.append(dataset)
  # Do fuzzy serach to the all reactions to match the search text.
  m = process.extract(text, reaction, limit=number)  
  # Save the serach result.
  for j in range(len(reaction)):
      for best in m:
          if best[0] in reaction[j]:
            if check== 0:
              reactionnew.append(best[0])
              datafromnew.append(datafrom[j])
              logknew.append(logk[j])
              namenew.append(name[j])
              check = check+1
            else:
                for o in range(len(reactionnew)):
                    if best[0] in reactionnew[o] and logk[j] in logknew[o]:
                        checkifexist = True
                if checkifexist == False:
                       reactionnew.append(best[0])
                       datafromnew.append(datafrom[j])
                       logknew.append(logk[j])
                       namenew.append(name[j]) 
                checkifexist = False
               
  data = {"Reaction":reactionnew,"logk":logknew,"database":datafromnew,"name":namenew}
           
  dataframe=DataFrame(data)
        
  dataframe.to_csv(table,index=False,sep=',')      
  fileList = os.listdir(dirlast+ '/table')
  for fl in fileList:
     if os.path.getsize(dirlast+ '/table/'+fl) == 0:
                os.remove(dirlast+ '/table/'+fl)
                return False
  return True

                     






