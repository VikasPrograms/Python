
def Add(*Values):
    print(type(Values))     # class tuple
    print("Number of arguments are : ",len(Values))

    Sum = 0

    for no in Values:
        Sum = Sum + no

    return Sum

def AddX(*Values):
    Sum = 0
    for i in range(0, len(Values),1):
        Sum = Sum + Values[i]

    return Sum

def main():
    Ans = Add(10,11,15,6)
    print("Addition is : ",Ans)

    Ans = AddX(11,15,22)
    print("Addition is : ",Ans)

if __name__ == "__main__":
    main()