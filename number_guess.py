"""

Secret number (Computer) 1-10

User - guess a number

true - you won
false - you lost with number

"""

import random
secret_number = random.randint(1,100)
#print(secret)

user_number = int(input('Please input your guessed number : '))

if user_number == secret_number:
    print('you won')
else:
    print(f"you lost... the number was {secret_number}")
