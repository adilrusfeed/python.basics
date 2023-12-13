file = open("Fileprogram.txt", "w")
file.write("it is my challenge,this is random data")
file.close()



file=open("Fileprogram.txt","a")
file.write("\nthis is appended text")
file.close()

file=open("Fileprogram.txt","r")
content=file.read()
print(content)
file.close()

