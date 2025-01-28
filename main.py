from art import text2art
from os import system
from colorama import init as cinit, Fore
from requests import get
import json

ping = lambda x: system(f"ping {x}")
clear = lambda: system("cls")
ENTER_URL_TEXT = "Enter the URL: "

print("loading cookies in file cookies.json and params in params.json")
cookies = json.load(open("cookies.json"))
params = json.load(open("params.json"))

def clear_and_show_logo_and_choices():
    clear()
    print(text2art("InterFuncs"))
    
    print("1. exit\n2. ping\n3. get site status code\n4. get text (html or json) on site\n5. get is ok on site ")

def main():
    while True:
        clear_and_show_logo_and_choices()
        cmd = input(">>> ")
        try:
            if cmd == "1":
                break
            elif cmd == "2":
                ip = input("Enter the IP address: ")
                ping(ip)
            elif cmd == "3":
                url = input(ENTER_URL_TEXT)
                response = get(url, cookies=cookies, params=params)
                
                print(response.status_code)
            elif cmd == "4":
                url = input(ENTER_URL_TEXT)
                response = get(url, cookies=cookies, params=params)
                
                with open("text.txt", 'w', encoding='utf-8') as f:
                    f.write(response.text)
                print("text saved in text.txt")
            elif cmd == "5":
                url = input(ENTER_URL_TEXT)
                response = get(url, cookies=cookies, params=params)
                
                print(response.ok)
            print("Press enter to continue...")
            input()
        except Exception as e:
            print(Fore.RED + f"Error: {e}")
            print("Press enter to continue...")
            input()
if __name__ == "__main__":
    clear()
    cinit(autoreset=True)
    main()