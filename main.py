import os
import time
from time import sleep

print('Want to install all packages? y/n')
i = input()

if i == 'y':
 os.system('python installer.py')


import requests
import colorama
import urllib3
from colorama import Fore



print(Fore.LIGHTBLACK_EX + ' __    ____  ____  ____  ___  ____  _  _ ')
print(Fore.LIGHTWHITE_EX + '(  )  (_  _)( ___)(_  _)/ __)( ___)( \( )')
print(Fore.LIGHTBLACK_EX + ' )(__  _)(_  )__)   )( ( (_-. )__)  )  ( ')
print(Fore.LIGHTWHITE_EX + '(____)(____)(__)   (__) \___/(____)(_)\_)) Created by t.me/liftium')
time.sleep(0.1)
os.system('cls')
print(Fore.LIGHTBLACK_EX + ' __    ____  ____  ____  ___  ____  _  _ ')
print(Fore.LIGHTBLACK_EX + '(  )  (_  _)( ___)(_  _)/ __)( ___)( \( )')
print(Fore.LIGHTBLACK_EX + ' )(__  _)(_  )__)   )( ( (_-. )__)  )  ( ')
print(Fore.LIGHTWHITE_EX + '(____)(____)(__)   (__) \___/(____)(_)\_)) Created by t.me/liftium')
time.sleep(0.1)
os.system('cls')
print(Fore.LIGHTBLACK_EX + ' __    ____  ____  ____  ___  ____  _  _ ')
print(Fore.LIGHTWHITE_EX + '(  )  (_  _)( ___)(_  _)/ __)( ___)( \( )')
print(Fore.LIGHTBLACK_EX + ' )(__  _)(_  )__)   )( ( (_-. )__)  )  ( ')
print(Fore.LIGHTBLACK_EX + '(____)(____)(__)   (__) \___/(____)(_)\_)) Created by t.me/liftium')
time.sleep(0.1)
os.system('cls')
print(Fore.LIGHTBLACK_EX + ' __    ____  ____  ____  ___  ____  _  _ ')
print(Fore.LIGHTWHITE_EX + '(  )  (_  _)( ___)(_  _)/ __)( ___)( \( )')
print(Fore.LIGHTWHITE_EX + ' )(__  _)(_  )__)   )( ( (_-. )__)  )  ( ')
print(Fore.LIGHTWHITE_EX + '(____)(____)(__)   (__) \___/(____)(_)\_)) Created by t.me/liftium')
time.sleep(0.1)
os.system('cls')
print(Fore.LIGHTBLACK_EX + ' __    ____  ____  ____  ___  ____  _  _ ')
print(Fore.LIGHTWHITE_EX + '(  )  (_  _)( ___)(_  _)/ __)( ___)( \( )')
print(Fore.LIGHTBLACK_EX + ' )(__  _)(_  )__)   )( ( (_-. )__)  )  ( ')
print(Fore.LIGHTWHITE_EX + '(____)(____)(__)   (__) \___/(____)(_)\_)) Created by t.me/liftium')
print(' ')
time.sleep(1)
print('Paste your license code: (you can purchase it here for 5$ - t.me/liftium)')
def license():
    # The list with all keys.
    keys = requests.get('https://liftium.space/secure/txt/88d10fs.txt').text
    # keys = ["key1", "key2", "key3"]

    # License key from user.
    keyfromuser = input('')

    for key in keys.splitlines():
        if key == keyfromuser:
            # Code when key match.
            return

    # Code if the key don't match.
    exit()
license()
time.sleep(1)
os.system('cls')
print(Fore.LIGHTBLACK_EX + ' __    ____  ____  ____  ___  ____  _  _ ')
print(Fore.LIGHTWHITE_EX + '(  )  (_  _)( ___)(_  _)/ __)( ___)( \( )')
print(Fore.LIGHTBLACK_EX + ' )(__  _)(_  )__)   )( ( (_-. )__)  )  ( ')
print(Fore.LIGHTWHITE_EX + '(____)(____)(__)   (__) \___/(____)(_)\_)) Created by t.me/liftium')
print('----------------------- MENU ----------------------------')
print(Fore.LIGHTBLACK_EX + '1. Instagram 4. Google 7. Microsoft 10. Mail 13. Stripe Key')
print(Fore.LIGHTBLACK_EX + '2. Facebook 5. Twitter 8. Steam 11. Phone Number 14. Paypal')
print(Fore.LIGHTBLACK_EX + '3. Discord Token 6. Discord Promotion 9. Tiktok 12. Address 15. Discord Nitro')
select = input(Fore.LIGHTYELLOW_EX + ':')

if select == '1':
 os.system('cd modules')
 os.system('python ig.py')

if select == '2':
 os.system('cd modules')
 os.system('python fb.py')
 
if select == '3':
 os.system('cd modules')
 os.system('python dc.py')

if select == '4':
 os.system('cd modules')
 os.system('python ggl.py')

if select == '5':
 os.system('cd modules')
 os.system('python twt.py')

if select == '6':
 os.system('cd modules')
 os.system('python dcprom.py')

if select == '7':
 os.system('cd modules')
 os.system('python mcrst.py')

if select == '8':
 os.system('cd modules')
 os.system('python steam.py')


if select == '9':
 os.system('cd modules')
 os.system('python tt.py')

if select == '10':
 os.system('cd modules')
 os.system('python mail.py')

if select == '11':
 os.system('cd modules')
 os.system('python ph.py')

if select == '12':
 os.system('cd modules')
 os.system('python addy.py')

if select == '13':
 os.system('cd modules')
 os.system('python sk.py')

if select == '14':
 os.system('cd modules')
 os.system('python pp.py')

if select == '15':
 os.system('cd modules')
 os.system('python nitro.py')
