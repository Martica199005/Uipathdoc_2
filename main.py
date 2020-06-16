import os
import pathlib
import sys
import math


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
      if 'InvokeWorkflowFile' in line:
        stringa=line.split('"')
        if len(stringa)>1:
          print('Invoke workflow: {}'.format(stringa[3]))
  return None


def bool_search(path):
  list=[]
  with open(path,'r') as f:
    tag = input("Enter attribute to search\n ")
    list.append(tag)
    if tag in f.read():
      founded=True
    else:
      founded=False
      print('Not present')
    list.append(founded)
  return list



#Search for a tag/attribute
def search_attribute(path,result):
  if result[1]==True:
    with open(path,'r') as f:
      tag=result[0]
      #tag = input("Enter attribute to search\n ")
      for line in f:
        if tag in line:
            print("{} is in {}".format(tag,line))

          
#Show only subdirectories       
def display_only_subdir(path):
  dirs=[]
  for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
      dirs.append(entry)
  return dirs



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

def print_list(list):
  if list:
    listOfFiles=list
    for elem in listOfFiles:
      if not ".git" in elem:
        count=elem.count('/')
        if count>1:
          space=count*"\t"
          identation=space+str(elem)
          print(identation)
        if elem.endswith(".txt") or elem.endswith(".xaml"):
          print("")
          #result=bool_search(elem)
          #search_attribute(elem,result)
          display_annotations(elem)
        print ("*"*len(str(elem))) 

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
  if not ".git" in elem:
    count=elem.count('/')
    if count>1:
      space=(count)*"\t"
      identation=space+str(elem)
      print(identation)
    if elem.endswith(".txt") or elem.endswith(".xaml"):
      print("")
      #result=bool_search(elem)
      #search_attribute(elem,result)
      #display_annotations(elem)
    print ("*"*len(str(elem))) 


# Save a reference to the original standard output  
original_stdout = sys.stdout 

#Write the result in document.txt
with open('document.txt', 'w') as f:
  # Change the standard output to the file we created.
  sys.stdout = f 
  print_list(listOfFiles)
  sys.stdout = original_stdout # Reset the standard output to its original value




  
#identation for subdirectories: count number of /

  
  






     
  


     
      


