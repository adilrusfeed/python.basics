obj=["aa","bb","cc"]
for i in obj:
    print(i)
else:
    print("nothing")


for i in range(10):
    if i == 5:
        break
    print(i)
else:
    print("n")


for i in range(10,16):
    print(i,end=",")