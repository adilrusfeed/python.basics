# t=int(input("enter a num"))
# if(t==1):
#     print("january")
# elif(t==2):
#     print("february")
# elif(t==3):
#     print("march")
# elif(t==4):
#     print("april")
# elif (t == 5):
#     print("may")
# elif (t == 6):
#     print("june")
# elif (t == 7):
#     print("july")
# elif(t==8):
#     print("august")
# elif(t==9):
#     print("september")
# elif(t==10):
#     print("october")
# elif(t==11):
#     print("november")
# elif(t==12):
#     print("december")
# else:print("invalid number\ntype 1-12")


def calculate(principle, year, rate):
    intrest = (principle * year * rate) / 100
    return intrest


principle = int(input("enter the principle value: "))
year = int(input("enter the no.of year: "))
rate = int(input("enter the rateP: "))
total = calculate(principle, year, rate)
print(total)
