# Accept the N numbers from user and return the addition of this numbers.


class Numbers:
    def __init__(self):
        self.Size = 0                            # local variable
        self.Arr = list()

    def Accept(self):
        print("Enter how many elements you want : ")
        self.Size = int(input())

        print("Please enter the elements")
        Value = 0                               # local variable
        for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
        print("Elements from list are Store : ")
        for i in range(0,self.Size):
            print(self.Arr[i])

    def Summation(self):
        Sum = 0                                 # local variable
        for i in range(0,self.Size):
            Sum = Sum + self.Arr[i]
        return Sum

def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()

    Output = obj.Summation()
    print("Summation of all elements is : ",Output)

if __name__ == "__main__":
    main()