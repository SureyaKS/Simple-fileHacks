"""
Simple code to handle redundant task.

Inputs :

1. Folder to process : D:/myFolder/folder having all files/
	* It would iterate through all sub-folders and files.

2. File extension to search: 'csv' or 'pdf' or 'xlsx' (or any valid file format)

3. Search Pattern:  Type any words that a file has, so that, the code can match the file you want.

	Sample: If I want to serach files having string  'ask' then the input would be just : ask. (CASE SENSITIVE) 

"""

import os,sys
import shutil


#INPUTS AND VALIDATIONS
folderPath = raw_input("Enter the main directory to search : ")

isDirPresent = os.path.isdir(filesDirectory)
if(isDirPresent==False):
	print "Error: Invalid directory, No such directory to search"
	print "Terminatting the program"
	sys.exit()

folderPath = folderPath.replace('\\','/')
if folderPath[-1] != '/':
	folderPath = folderPath+'/'

pdfs = []
TO=raw_input("Enter the destination folder where the PDF's have to be stored : ")

TO = TO.replace('\\','/')

if TO[-1] != '/':
	TO = TO+'/'


nameStartsWith = raw_input("Find files, having the word :  ")

extension = raw_input("Enter the extension of the file you want to serach : ('csv' or 'pdf',etc...) ") 

if extension[0]!='.':
	extension = '.'+extension

# END OF VALIDATIONS

i=0;
for subdir, dirs, files in os.walk(folderPath):
   for hasNext in subdir:
        for file in files:
            if extension in file:
                pdfs.append(os.path.join(subdir, file))
    i = i+1

if(i=0):
	print "The directory is empty"
	print "Terminatting the program"
	sys.exit()


for fileName in pdfs:
    
    if nameStartsWith in fileName :
        temp = fileName.split('/')[-1]
        shutil.copy2(fileName, TO+temp)
        print "Transferred "+fileName+" to destination folder "
        
    
