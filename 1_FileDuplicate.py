#---------------------------------------------------------------------------------
# >>>>> Steps to folow while programming :-

# Step 1  Understand the problem statement
# Step 2  Write the algorithm
# Step 3  Decide the programming language
# Step 4  Write the program
# Step 5  Test the program
#---------------------------------------------------------------------------------


#---------------------------------------------------------------------------------
# Required Python Packages
#---------------------------------------------------------------------------------

#---------------------------------------------------------------------------------
# Automation script which accept directory name from user and 
# display all names of duplicate files from that directory.
#---------------------------------------------------------------------------------

from sys import *
import os
import hashlib

#---------------------------------------------------------------------------------
# Function Name : hashfile
# Description : Open the path
# Author : Bade Vikas Vasudeo
# Date : 05/06/2022
#---------------------------------------------------------------------------------

def hashfile(path, blocksize = 1024):
    # Open Files
    fd = open(path, 'rb')
    hasher = hashlib.md5()

    # Read the Files
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    # Close the Files
    fd.close()

    return hasher.hexdigest()

#---------------------------------------------------------------------------------
# Function Name : FindDuplicate
# Description : Find the Duplicate Files
# Author : Bade Vikas Vasudeo
# Date : 05/06/2022
#---------------------------------------------------------------------------------

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}
    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print(("Invalid Path"))

#---------------------------------------------------------------------------------
# Function Name : PrintDuplicate
# Description : list the duplicate file
# Author : Bade Vikas Vasudeo
# Date : 05/06/2022
#---------------------------------------------------------------------------------

def PrintDuplicate(dict1):
    results = list(filter(lambda x : len(x) > 1,dict1.values()))

    if len(results) > 0:
        # Found the Duplicates Files
        print("Duplicates Found : ")
        
        # print the identical files
        print("The following files are identical.")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print('\t\t%s' % subresult)
    else:
        print("No duplicate files found.")

#---------------------------------------------------------------------------------
# Function Name : main
# Description : main function from where execution starts
# Author : Bade Vikas Vasudeo
# Date : 05/06/2022
#---------------------------------------------------------------------------------

def main():
    print("---------------------------------------- By Bade Vikas ----------------------------------------")
    print("-------------- Application Name : Duplicate File Displayii Using Automation Script --------------")
    print("----------------------------------- File name : "+argv[0]+" -----------------------------------")

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display sizes of files")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory Extention")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error : Invalid datatype of input")

#---------------------------------------------------------------------------------
    # Application Starter
#---------------------------------------------------------------------------------

if __name__ == "__main__":
    main()