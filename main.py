#Password Generator Project
import random
let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nlet= int(input("How many letters would you like in your password?\n")) 
nsym = int(input(f"How many symbols would you like?\n"))
nnum = int(input(f"How many numbers would you like?\n"))
plet = []
psym = []
pnum = []
for n in range(0,nlet):
    plet.append(random.choice(let))
for n in range(0,nsym):
    psym.append(random.choice(sym))
for n in range(0,nnum):
    pnum.append(random.choice(num))
password = plet + psym + pnum
random.shuffle(password)
print("Here is your password: ",end="")
for i in password:
   print(i,end="")