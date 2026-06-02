import random
print("Welcome to python password generator")
alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
nr_letters = int(input(f"How many letters do you want? "))
nr_symbols = int(input(f"How many symbols do you want? "))
nr_numbers = int(input(f"How many numbers do you want? "))
for letter in range(nr_letters):
    password.append (random.choice(alphabets))
for letter in range(nr_symbols):
    password.append (random.choice(symbols))
for symbol in range(nr_numbers):
    password.append (random.choice(numbers))
random.shuffle(password)
final_password = "".join(password)
print("Your password is:", password)



