import random, string
password_length = int(input("How long does ur password need to be ? Please tell me in numbers..."))
password_characters = string.ascii_letters + string.digits + string.punctuation
password = []
for x in range(password_length):
    password.append(random.choice(password_characters))
print(''.join(password))
