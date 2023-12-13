def function1(a, b):
    print(a / b)


try:
    function1(10, 0)
except:
    print("num cannot divide by 0")

# -------------------------------------------------------------

# a = [12, 435, 6456, 3, 32]
# try:
#     print(a[6])
# except:
#     print("index error")
#     s=(int(input("enter the index 0-3 : ")))
#     print(a[s])

# ------------------------------------------------------------------

# def sample(x,y):
#     sum=x+y
#     return sum
# a=12
# b=34
# z=sample(a,b) #if the a or b replaced by any other letter(variable) ,it is name error
# print(z)
