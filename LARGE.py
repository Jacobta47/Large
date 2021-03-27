#*****************************************************************
#JACOB T. ARMENTROUT *********************************************
#*****************************************************************

import os

filename = 'large.txt'

open(filename, 'x').close()

f = open(filename, 'w+')

str1 = "1.0."

i = 0

u = 1000000000

def size():
    return os.path.getsize("large.txt")

while i < u:
    f.write(str1)
    i += 1
    end = "Size: " +  '{:,.0f}'.format(size()) + " bytes"
    out = "Progress: " + '{:,.0f}'.format(i) + " / " + '{:,.0f}'.format(u)
    print(out + " | " + end)

f.close()
print(end + " finished.")

