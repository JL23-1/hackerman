import names
import random
import string
from os import system, name
from time import sleep    
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()
print(
    'Password\n'
)
passwd = input('> ')
clear()
print(
    'ACCESS DENIED'
)
sleep(1)
clear()
print(
    'Password\n'
)
passwd = input('> ')
clear()
print(
    'ACCESS DENIED'
)
sleep(1)
clear()
print(
    'Password\n'
)
passwd = input('> ')
clear()
print(
    'ACCESS GRANTED'
)
sleep(1)
clear()
while True:
    print(random.choice(string.digits) + random.choice(string.digits) + '.' + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + '.' + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + '.' + random.choice(string.digits) + random.choice(string.digits) + ' -- ' + names.get_full_name())
    sleep(0.5)
