for i in range(3):
    for x in range(1,5):
        print(x, end=",")
    print()

# patterns------------------------------------------------------------------------------------------------

for i in range(4):
    for j in range(i):
        print("*", end=" ")
    print()


for i in range(1,7):
    for j in range (i):
        print("*",end="")
    print()


x = [22, 33]
y = [44, 55]
for i in x:
    for j in y:
        print(i, j)#22 44    22 55    33 44   33 55
