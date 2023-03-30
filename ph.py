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

url = "https://virtual-number.p.rapidapi.com/api/v1/e-sim/country-numbers"

querystring = {"countryId":"1"}

headers = {
	"X-RapidAPI-Key": "5816a45f46mshd1655e9c2ff8b28p1e4707jsn35223d1d69af",
	"X-RapidAPI-Host": "virtual-number.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

url2 = "https://virtual-number.p.rapidapi.com/api/v1/e-sim/view-messages"

querystring2 = {"countryId":"1","number": response}

headers2 = {
	"X-RapidAPI-Key": "5816a45f46mshd1655e9c2ff8b28p1e4707jsn35223d1d69af",
	"X-RapidAPI-Host": "virtual-number.p.rapidapi.com"
}

response2 = requests.request("GET", url2, headers=headers2, params=querystring2)

print('Phone Number:' + response.text)
print(' ')
print(response2.text)
ref = input('If you want to refresh, press enter')
os.system('cls')
print('Phone Number:' + response.text)
print(' ')
print(response2.text)

time.sleep(30)