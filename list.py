from builtins import print

x = ["fast", 78, "yy"]

print(len(x))
print(x)
print(x[2])
print(x[-2])

x[1]=200
print(x)
x.append("inmakes")
print(x)

x.insert(1,"furious")
print(x)
print(len(x), "is length the length of list")
print(x.index("inmakes"))
x.pop(1)
print(x)
x.clear()
print(x)
