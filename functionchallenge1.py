# def final-price(price_x, price_y):
#     price = (price_x / price_y ** 2)
#     return price
#
# x = int(input("enter price of x:  "))
# y = int(input("enter price of y:  "))
# result = final-price(x, y)
# print("Final Price is:", result)


# ---------------------------------------------------------------

# def total_sum(num1, num2):
#     total = (num1 + num2)
#     return total
#
#
# x = int(input("enter num1:  "))
# y = int(input("enter num2:  "))
# result = total_sum(x, y)
# print("sum is: ", result)

# --------------------------------------------------

def add(a, b):
    return a + b
def square(c):
    return c * c
print(add(2, 4))
print(square(10))

print(square(add(a=1,b=2)))