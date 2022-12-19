# Display Even and Odd Numbers in serial

def DisplayEven(No):
    for i in range(1,No,1):
        if(i % 2 == 0):
            print("Even number : ",i)

def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Odd number : ",i)

def main():
    print("Demonstration of Serial programming : ")
    DisplayEven(2000)
    DisplayOdd(2000)

if __name__ == "__main__":
    main()