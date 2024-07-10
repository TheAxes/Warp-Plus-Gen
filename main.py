import datetime
import random
import string
import time
import os
import httpx
import colorama
from colorama import Fore

os.system('cls' if os.name == 'nt' else 'clear')

banner = """

 _                                                _                       
/   | |                   | |/ | |                | |  | |                     
| /  /| |          _  | | || | __      | |  | |      __ | | 
| |    | |    /  | | | |/ ` |  | |/ ` | '__/  \ | |/| |/ ` | '__| ' _   |
| _/| || () | || | (| | | | | (_| | | |  / \  /\  / (| | |  | |) |||  
 ___/___/_/ _,|_,|| ||_,||  ___|  /  / _,||  | ._/      
                                                                        | |         
                                                                        ||         
"""
print(f"{Fore.LIGHTCYAN_EX}{banner}{Fore.RESET}")
print("Made By @TheAxes")

def genString(stringLength):
    try:
        letters = string.asciiletters + string.digits
        return ''.join(random.choice(letters) for  in range(stringLength))
    except Exception as error:
        print(error)

# Function to generate a random digit string
def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join(random.choice(digit) for _ in range(stringLength))
    except Exception as error:
        print(error)

def process_request(referrer):
    try:
        install_id = genString(22)
        body = {
            "key": f"{genString(43)}=",
            "install_id": install_id,
            "fcm_token": f"{install_id}:APA91b{genString(134)}",
            "referrer": referrer,
            "warp_enabled": False,
            "tos": f"{datetime.datetime.now().isoformat()[:-3]}+02:00",
            "type": "Android",
            "locale": "es_ES",
        }
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'api.cloudflareclient.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'
        }

        with httpx.Client() as client:
            response = client.post(f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg', json=body, headers=headers)

        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] 1 GB {Fore.RESET}")
            return True
        else:
            return False
    except Exception as error:
        time.sleep(1)
        return False

def estimate_total_time(count):
    total_time = (count * 11) + ((count - 1) * 4.2) #brokwn mths done here
    return total_time
count = int(input("How Many GB You Want: "))
user_id = input("User ID: ")
goods = 0
expected_total_time = estimate_total_time(count)

print(f"Estimated total time to complete {count}GB for {user_id}: {expected_total_time} seconds")

start_time = time.time()
while goods < count:
        data = process_request(user_id)
        if data is True:
            goods+=1
            time.sleep(11)
        else:
            time.sleep(2)
elapsed_time = time.time() - start_time
os.system('cls' if os.name == 'nt' else 'clear')
print(f"{Fore.LIGHTCYAN_EX}{banner}{Fore.RESET}")
print(f"{Fore.GREEN}Added {goods} GB TO {user_id}{Fore.RESET}")
print(f"Total time taken: {elapsed_time:.2f} seconds")
os.system("exit")
