import os
from os import system
system("clear")
import random

usernumber = []
compnumber = []
score =[]
i = usernumber
while len(usernumber) < 5:
    unum = input(" Please enter 5 numbers ranging from 1-70 ")
    
    if unum.isdigit() == False:
        print ("Please enter a number... ")
    elif int(unum) > 70:
        print("70 or please... ")
    elif int(unum) < 1:
        print("1 or above please... ")
    else:
        
        usernumber.append(int(unum))
        print (usernumber)

for i in range(5):
    rand=random.randint(1,70)
    compnumber.append(rand)


print(compnumber)
final = set(usernumber) & set(compnumber)
sorted(final)
print(len(final))
print(list(final))

if len(final) == 5:
    print(" You matched all 500p ")
elif len(final) == 4 :
    print(" You matched 4 , 100p")
elif len(final) == 3 :
    print(" You matched 3 , 30p")
elif len(final) == 2 :
    print(" You matched 2 , 4p")
elif len(final) == 1 :
    print(" You matched 1 , 1p")
else:
    print(" You did not match a single one... ")