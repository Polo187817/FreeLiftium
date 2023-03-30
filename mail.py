import random
import colorama
from colorama import Fore
import os
import time
import requests

os.system('cls')

print(Fore.LIGHTBLACK_EX + ' __    ____  ____  ____  ___  ____  _  _ ')
print(Fore.LIGHTWHITE_EX + '(  )  (_  _)( ___)(_  _)/ __)( ___)( \( )')
print(Fore.LIGHTBLACK_EX + ' )(__  _)(_  )__)   )( ( (_-. )__)  )  ( ')
print(Fore.LIGHTWHITE_EX + '(____)(____)(__)   (__) \___/(____)(_)\_)) Created by t.me/liftium')
time.sleep(2)

mai = ['tower', 'katie', 'john', 'steel', 'carl', 'jake', 'please', 'david', 'samuel', 'carlos', 'javis', 'angola']
mai2 = ['salmon', 'yubo', 'neba', 'souls', 'cameson', 'paul', 'goodman', 'heisenberg', 'somalio', 'herta', 'jamel']
mai3 = ['h32', '8ds', '01', '71', '831', '912', '66', '99', '91', '11', '77', '42', '98', '97', '2004', '2001', '2002']
domain = ['@gmail.com', '@outlook.com', '@yahoo.com', '@mail.ru', '@hotmail.com', '@icloud.com']



def custom_print(mail = random.choice(mai) + random.choice(mai2) + random.choice(mai3) + random.choice(domain), log_file='./mails/mails.txt'):
    print(mail)
    with open(log_file, 'a') as of:
        of.write(mail + '\n')

custom_print()

print('Saved to mails.txt')

time.sleep(1)
os.system('python mail.py')
