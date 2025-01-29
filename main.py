from art import text2art
import os
from requests import get
from rich.console import Console
from rich.panel import Panel
import json
from rich.syntax import Syntax

console = Console()

ping = lambda x: os.system(f"ping {x}")
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
ENTER_URL_TEXT = "Enter the URL: "

print("loading cookies in file cookies.json and params in params.json")
cookies = json.load(open("cookies.json"))
params = json.load(open("params.json"))

def clear_and_show_logo_and_choices():
    clear()
    console.print("[red]" + text2art("InterFuncs"))
    
    console.print(Panel.fit("1. exit\n2. ping\n3. get site status code\n4. get site text (html or json)\n5. get site is ok\n6. get site headers\n7. get site json\n8. check site availability\n9. get site content"))

def handle_ping():
    ip = input("Enter the IP address: ")
    ping(ip)

def handle_get_status_code():
    url = input(ENTER_URL_TEXT)
    response = get(url, cookies=cookies, params=params)
    print(response.status_code)

def handle_get_text():
    url = input(ENTER_URL_TEXT)
    response = get(url, cookies=cookies, params=params)
    with open("text.txt", 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("text saved in text.txt")
    content_type = response.headers.get('Content-Type', '')
    if 'html' in content_type:
        lang = "html"
    elif 'json' in content_type:
        lang = "json"
    else:
        lang = "text"
    console.print(Syntax(response.text, lang))

def handle_get_is_ok():
    url = input(ENTER_URL_TEXT)
    response = get(url, cookies=cookies, params=params)
    print(response.ok)

def handle_get_headers():
    url = input(ENTER_URL_TEXT)
    response = get(url, cookies=cookies, params=params)
    print(response.headers)

def handle_get_json():
    url = input(ENTER_URL_TEXT)
    response = get(url, cookies=cookies, params=params)
    try:
        json_data = response.json()
        console.print(Syntax(json.dumps(json_data, indent=4), "json"))
    except ValueError:
        console.print("[red]Error: Response is not in JSON format")

def handle_check_site_availability():
    url = input(ENTER_URL_TEXT)
    response = get(url, cookies=cookies, params=params)
    if response.status_code == 200:
        print("Site is available")
    else:
        print(f"Site is not available, status code: {response.status_code}")

def handle_get_content():
    url = input(ENTER_URL_TEXT)
    response = get(url, cookies=cookies, params=params)
    
    print(response.content)
    with open("text.txt", 'w') as f:
        f.write(response.content)
    print("content saved in text.txt")

def main():
    while True:
        clear_and_show_logo_and_choices()
        cmd = console.input("[green]>>> ")
        try:
            if cmd == "1":
                break
            elif cmd == "2":
                handle_ping()
            elif cmd == "3":
                handle_get_status_code()
            elif cmd == "4":
                handle_get_text()
            elif cmd == "5":
                handle_get_is_ok()
            elif cmd == "6":
                handle_get_headers()
            elif cmd == "7":
                handle_get_json()
            elif cmd == "8":
                handle_check_site_availability()
            elif cmd == "9":
                handle_get_content()
            print("Press enter to continue...")
            input()
        except Exception as e:
            console.print(f"[red]Error: {e}")
            print("Press enter to continue...")
            input()

if __name__ == "__main__":
    clear()
    main()