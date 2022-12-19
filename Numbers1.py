# Accept the N numbers from user and return the Display of this numbers list.

class Numbers:
    def __init__(self):
        self.Size = 0
        self.Arr = list()       # blank list generate using array

    def Accept(self):
        print("Enter how many elements you want : ")
        self.Size = int(input())        # Accept the users numbers of elements

        print("Please enter the elements")
        Value = 0
        for i in range(0,self.Size):        # Add this Total elements
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
        print("Elements from list are : ")
        for i in range(0,self.Size):        # Display The elements in list format
            print(self.Arr[i])

def main():
    obj = Numbers()
    obj.Accept()
    obj.Display()

if __name__ == "__main__":
    main()