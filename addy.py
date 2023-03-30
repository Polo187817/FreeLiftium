import requests
import colorama
import urllib3
from colorama import Fore
import os
import time

print(Fore.LIGHTBLACK_EX + ' __    ____  ____  ____  ___  ____  _  _ ')
print(Fore.LIGHTWHITE_EX + '(  )  (_  _)( ___)(_  _)/ __)( ___)( \( )')
print(Fore.LIGHTBLACK_EX + ' )(__  _)(_  )__)   )( ( (_-. )__)  )  ( ')
print(Fore.LIGHTWHITE_EX + '(____)(____)(__)   (__) \___/(____)(_)\_)) Created by t.me/liftium')
print(' ')
time.sleep(1)

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

url = "https://randomuser.me/api/"

response = requests.request("GET", url, headers=headers)

print(response.text)

os.system('pause')