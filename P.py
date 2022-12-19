from sys import *

def Addition(A,B):
    iAns = 0
    iAns = A + B
    return iAns

def main():
    print("Welcome to : ",argv[0])

    if(len(argv) == 2):
        if(argv[1] == "--U"):
            print("Use the application as : ")
            print("python Name_of_Application First- number")