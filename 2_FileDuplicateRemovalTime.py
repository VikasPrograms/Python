
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
# remove duplicate files from that directory.
#---------------------------------------------------------------------------------

from sys import *
import os
import hashlib
import time

#---------------------------------------------------------------------------------
# Function Name : DeleteFiles
# Description : Delete the Duplicate Files
# Author : Bade Vikas Vasudeo
# Date : 20/07/2022
#---------------------------------------------------------------------------------

def DeleteFiles(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))

    icnt = 0

    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    os.remove(subresult)
            icnt = 0
    else:
        print("No duplicate files found.")    

#---------------------------------------------------------------------------------
# Function Name : hashfile
# Description : Open the path
# Author : Bade Vikas Vasudeo
# Date : 20/07/2022
#---------------------------------------------------------------------------------

def hashfile(path, blocksize = 1024):
    # Open the File path
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    # Close the File path
    afile.close()

    return hasher.hexdigest()

#---------------------------------------------------------------------------------
# Function Name : FindDuplicate
# Description : Find the Duplicate Files
# Author : Bade Vikas Vasudeo
# Date : 20/07/2022
#---------------------------------------------------------------------------------

def findDup(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is : "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid Path")

#---------------------------------------------------------------------------------
# Function Name : PrintDuplicate
# Description : list the duplicate file
# Author : Bade Vikas Vasudeo
# Date : 20/07/2022
#---------------------------------------------------------------------------------

def printResults(dict1):
    results = list(filter(lambda x : len(x) > 1, dict1.values()))       # filter(condition, provides)
    # data = list(filter(CheckEven, Arr))

    if len(results) > 0:
        # Found the Duplicates Files
        print('Duplicates Found :')

        # print the identical files
        print('The following files are duplicate')
        for result in results:
            for subresult in results:
                print('t\t%s' % subresult)
    else:
        print("No duplicate files found.")

#---------------------------------------------------------------------------------
# Function Name : main
# Description : main function from where execution starts
# Author : Bade Vikas Vasudeo
# Date : 20/07/2022
#---------------------------------------------------------------------------------

def main():
    print("---------------------------------------- By Bade Vikas ----------------------------------------")
    print("-------------- Application Name : Duplicate File Removal Using Automation Script --------------")
    print("----------------------------------- File name : "+argv[0]+" -----------------------------------")

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and delete duplicate files.")
        exit()

    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application Name AbsolutePath_of_Directory Extention")
        exit()

    try:
        arr = {}
        startTime = time.time()
        arr = findDup(argv[1])
        printResults(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print('Took %s seconds to evaluate.' % (endTime - startTime))

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

#---------------------------------------------------------------------------------
    # Application Starter
#---------------------------------------------------------------------------------

if __name__ == "__main__":
    main()