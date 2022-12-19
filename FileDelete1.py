import os

def Delete1_File(FileName):
    if(os.path.exists(FileName)):
        size = os.path.getsize(FileName)
        if(size == 0):
            os.remove(FileName)

        else:
            print("Are you sure to delete the file ? Y/N")
            option = input()
            if(option == "Y" or option == "y"):
                os.remove(FileName)
            else:
                print("File deletion process stoped.")
    else:
        print("There is no such file")
    

def main():

    print("Enter the file name to create : ")
    Name = input()

    Delete1_File(Name)

if __name__ == "__main__":
    main()