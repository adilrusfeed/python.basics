x= {
    "chair": 500,
    "table": 2000,
    "stool": 100,
    400:"stool"
}
print(x)
print(x[400])
print(len(x))
x.pop("chair")   # to remove the  key
print(x)
x.update({"chair":500})   # to add the  key
print(x)
x.popitem()     # to delete last key
print(x)
