
def Area(Radious, PI = 3.14):
    Result = PI * Radious * Radious
    return Result

def main():
    Rvalue = 10.5
    PIvalue = 3.14

    # Positional Arguments
    Ans = Area(Rvalue, PIvalue)     # Ans = Area(10.5, 3.14)
    print("Area of circle is : ",Ans)

    # Keyword Arguments
    Ans = Area(PI = PIvalue, Radious = Rvalue)     # Ans = Area(3.14,10.5)
    print("Area of circle is : ",Ans)

    # Positional Arguments and second is default
    Ans = Area(10.5)
    print("Area of circle is : ",Ans)

    # Keyword Arguments and second is Default
    Ans = Area(Radious = 10.5)
    print("Area of circle is : ",Ans)

    # Keyword Arguments
    Ans = Area(PI = 7.10, Radious = 10.5)
    print("Area of circle is : ",Ans)

if __name__ == "__main__":
    main()