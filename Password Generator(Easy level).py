import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
         'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','+']
print("Welcome to Password Generator\n")
a=int(input("How many letters would you like in your password? "))
b=int(input("How many numbers would you like in your password? "))
c=int(input("How many symbols would you like in your password? "))

password=""
for char in range(1,a+1):
    password+=random.choice(letters)
for char in range(1,b+1):
    password+=random.choice(numbers)
for char in range(1,c+1):
    password+=random.choice(symbols)
print(f"Here is your Password={password}")