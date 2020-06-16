import os
import pathlib
import sys


from os import listdir
from os.path import isfile, join

def display_annotations(path):
  with open(path,'r') as f:
    for line in f:
      if 'x:Class=' in line:
        stringa=line.split('"')
        print("The workflow type is {}.xaml\n".format(stringa[3]))
      if 'Annotation.AnnotationText' in line:
        stringa=line.split('"')
        #print(stringa)
        print("Annotation: {}".format(stringa[1]))
        l=len(stringa)
        if 'DisplayName' in line:
          stringa=line.split('"')
          print('Display Name: {}'.format(stringa[3]))
        print("Type {}\n".format(stringa[l-2]))
  return None



def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles  

#Gives current directory
basepath=os.getcwd()
print("Path: "+basepath)


dirName =basepath
# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)

# Get the list of all files in directory tree at given path
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(dirName):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    


# Print the files 
for elem in listOfFiles:
  print(elem)  
  print("")
  if elem.endswith(".txt") or elem.endswith(".xaml"):
    display_annotations(elem)
  print ("****************") 


# Save a reference to the original standard output  
original_stdout = sys.stdout 

#Write the result in document.txt
with open('document.txt', 'w') as f:
  sys.stdout = f # Change the standard output to the file we created.
  #print('This message will be written to a file.')
  for elem in listOfFiles:
    print(elem)  
    print("")
    if elem.endswith(".txt") or elem.endswith(".xaml"):
      display_annotations(elem)
    print ("****************")
  sys.stdout = original_stdout # Reset the standard output to its original value




    
    

  
  






     
  


     
      


