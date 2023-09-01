#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os.path 
import sys 
fname = input("Enter the filename : ")       
if not os.path.isfile(fname): 
    print("File", fname, "doesn't exists") 
    sys.exit(0) 
infile = open(fname, "r") 
lineList = infile.readlines() 
for i in range(20):                                      #change range as per file
    print(i+1, ":", lineList[i]) 
word = input("Enter a word : ") 
cnt = 0 
for line in lineList: 
    cnt += line.count(word) 
print("The word", word, "appears", cnt, "times in the file")


# 6-B
import os 
import sys 
import pathlib 
import zipfile 
dirName = input("Enter Directory name that you want to backup : ") 
if not os.path.isdir(dirName): 
    print("Directory", dirName, "doesn't exists") 
    sys.exit(0) 
curDirectory = pathlib.Path(dirName) 
with zipfile.ZipFile("myZip.zip", mode="w") as archive: 
    for file_path in curDirectory.rglob("*"): 
        archive.write(file_path, arcname=file_path.relative_to(curDirectory)) 
if os.path.isfile("myZip.zip"): 
    print("Archive", "myZip.zip", "created successfully") 
else: 
    print("Error in creating zip archive") 



