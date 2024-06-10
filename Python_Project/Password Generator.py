import random
print("****WELCOME TO RANDOM PASSWORD GENERATOR****")
letters= ["a", "b", "c", "d", "e","f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p", "q","r", "s","t"
          "u", "v", "w", "x", "y", "z", "A", "B",'C','D','E','F','G','H','I','J','K','L','M','N','O',
          'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers= ['0','1', '2', '3','4','5','6', '7', '8', '9']
symbol=['!', '@', '#', '$', '%', '%', '^', '&', '*', '(', ')', '-', '_', '+']

n_letters=int(input("How many letters would you like in your password?\n"))
n_numbers=int(input("How many numbers would you like in your password?\n"))
n_symbol=int(input("How many symbol would you like in your password?\n"))
password_list=[]

for i in range(1, n_letters+1):
   char =random.choice(letters)
   password_list += char

for i in range(1, n_numbers+1):
    char =random.choice(numbers)
    password_list += char

for i in range(1, n_symbol+1):
    char =random.choice(symbol)
    password_list += char
random.shuffle(password_list)
password=" "
for char in password_list:
    password += char
print("Your Random Password is: ",password)


