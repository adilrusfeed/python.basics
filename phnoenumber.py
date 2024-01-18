import  phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

user_number=input("enter number with country code ")
pn=phonenumbers.parse(user_number)

tz=timezone.time_zones_for_number(pn)
loc=geocoder.description_for_valid_number(pn,"en")
sp=carrier.name_for_valid_number(pn,"en")
print("TimeZone :",tz)
print("Location :",loc)
print("Carrier :",sp)

