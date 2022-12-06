import random
length = input("How long do you want your password to be? ")
password = ''
lowercase = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(length)):
  randChar = random.choice(lowercase)
  password = password + randChar
print("Weak Password: " + password)

password2 = ''
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(length)):
  randChar =random.choice(lowercase + uppercase)
  password2 = password2 + randChar
print("Moderate Password: " + password2)

password3 = ''
special = "1234567890`~!@#$%^&*()-_=+[]{}\|;:,./<>?"
for i in range(int(length)):
  randChar =  random.choice(lowercase + uppercase + special)
  password3 = password3  + randChar
print("Strong Password: " + password3)
