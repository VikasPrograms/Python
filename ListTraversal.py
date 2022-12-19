values = [10,20,30,40,50]

print("__________________")

print(values[0])        # starting point(0)
print(values[1])
    #displacement (between two syntax)
print(values[2])
print(values[3])
print(values[4])        # ending point(4)  (len(values)-1)

print("__________________")

for i in range(0,len(values),1):
            # _,1_ dila ny tari by default asatoch
            # means for i in range(0,len(values)):
    print(i)
    print(values[i])

print("__________________")

for no in values:
    print(no)

print("__________________")