# 4
# 3 + 2 + 1  ->  6

def Fact(No):
    if(No <= 0):
        return 0
    else:
        return (No + Fact(No - 1))

Ret = Fact(3)

print("Result is : ",Ret)
