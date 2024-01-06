def fact(x):
    if x==1:
        return 1
    else:
        return x*fact((x-1))

res=fact(4)
print(res)

# challenge------------------------------------------------

