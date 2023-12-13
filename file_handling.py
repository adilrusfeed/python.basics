# file read -------------------------------------
file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()

# to write----------------------
file = open("demo.txt", "w")
file.write("iam learning python.\n")
file.close()

file = open("demo.txt", "a")
file.write("in inmakes.")
file.close()

