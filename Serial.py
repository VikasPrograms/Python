
def Square(No):
    return (No*No)

def Cube(No):
    return(No*No*No)

def main():
    Data = [1,2,3,4,5]
    Result = []
    Result1 = []

    for Value in Data:
        Result.append(Square(Value))
        
    print("Result after square operation is ",Result)
    for Value in Data:
        Result1.append(Cube(Value))

    print("Result after cube operation is ",Result1)
    
if __name__ == "__main__":
    main()