import os

open('Large.txt', 'w').close()

File1 = open(r"C:\Users\jacob\Large.txt","w+")

str1 = "1.0."

i = 0

u = "/9999999999"

def size():
    return os.path.getsize("Large.txt")

end = int(size())

print(end)

while i < 9999999999:
    File1.write(str1)
    i += 9
    print(str(i) + u)

size()
print(end)