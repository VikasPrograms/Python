# Positional Arguments / Keyword arguments
def Add1(No1,No2):
    print("Value of No1 : ",No1)
    print("Value of No2 : ",No2)
    return No1 + No2

def Sub1(No1,No2):
    print("Value of No1 : ",No1)
    print("Value of No2 : ",No2)
    return No1 - No2

def Mult1(No1,No2,No3):
    print("Value of No1 : ",No1)
    print("Value of No2 : ",No2)
    print("Value of No3 : ",No3)
    return No1*No2*No3

def Div1(No1,No2):
    print("Value of No1 : ",No1)
    print("Value of No2 : ",No2)
    return No1/No2

def main():
    Ans = 0
    Ans = Add1(10,11)
    print("Addition is : ",Ans)

    Ans = Add1(No2 = 10, No1 = 11)
    print("Addition is : ",Ans)

    Ans = Sub1(No2 = 10,No1 = 11)
    print("Substraction is : ",Ans)

    Ans = Sub1(No1 = 10, No2 = 11)
    print("Substraction is : ",Ans)

    Ans = Mult1(No1 = 2, No2 = 3, No3 = 4)
    print("Multiplication is : ",Ans)

    Ans = Div1(No1 = 50, No2 = 5)
    print("Division is : ",Ans)

if __name__ == "__main__":
    main()