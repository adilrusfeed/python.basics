x= {
    "chair": 500,
    "table": 2000,
    "stool": 100,
    400:"stool"
}
print(x)
print(x["stool"])
print(len(x))
x.pop("chair")   # to remove the  key
print(x)
x.update({"chair": 500})   # to add the  key
print(x)
x.popitem()     # to delete last key
print(x)

for i in x.items():  # for iterating items
    print(i)

print(x.get("stool"))  # for print the specific key
print(x.get(100,"no key found"))
