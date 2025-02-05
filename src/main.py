from art import text2art
import os
import requests
from rich.console import Console
from rich.panel import Panel
import json
from rich.syntax import Syntax
from bs4 import BeautifulSoup

console = Console()

ping = lambda x: os.system(f"ping {x}")
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
ENTER_URL_TEXT = "Enter the URL: "
COOKIES_FILE = "../config/cookies.json"
PARAMS_FILE = "../config/params.json"
CONFIG_FILE = "../config/config.json"
with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
    CONFIG = json.load(f)

print("loading cookies in file cookies.json and params in params.json")
cookies = json.load(open(COOKIES_FILE))
params = json.load(open(PARAMS_FILE))

def clear_and_show_logo_and_choices():
    clear()
    console.print("[red]" + text2art("InterFuncs"))
    
    choices = {
        "1": "Exit",
        "2": "Ping",
        "3": "Get site status code",
        "4": "Get site text (html or json)",
        "5": "Get site is ok",
        "6": "Get site headers",
        "7": "Get site json",
        "8": "Check site availability",
        "9": "Get site content",
        "10": "Reset params",
        "11": "Reset cookies",
        "12": "Set params",
        "13": "Set cookies",
        "14": "Get css on site"
    }
    
    menu = "\n".join([f"{key}. {value}" for key, value in choices.items()])
    console.print(Panel.fit(menu, title="Menu", width=console.width))

def handle_ping():
    ip = input("Enter the IP address (without https:// or http://): ")
    with console.status("Pinging...", spinner=CONFIG['spinner']):
        ping(ip)

def handle_get_status_code():
    url = input(ENTER_URL_TEXT)
    with console.status("Getting status code...", spinner=CONFIG['spinner']):
        response = requests.get(url, cookies=cookies, params=params)
    print(response.status_code)

def handle_get_text():
    url = input(ENTER_URL_TEXT)
    with console.status("Getting text...", spinner=CONFIG['spinner']):
        response = requests.get(url, cookies=cookies, params=params)
        with open("text.txt", 'w', encoding='utf-8') as f:
            f.write(response.text)
    print("text saved in text.txt")
    content_type = response.headers.requests.get('Content-Type', '')
    if 'html' in content_type:
        lang = "html"
    elif 'json' in content_type:
        lang = "json"
    else:
        lang = "text"
    console.print(Syntax(response.text, lang))

def handle_get_is_ok():
    url = input(ENTER_URL_TEXT)
    with console.status("Checking is ok...", spinner=CONFIG['spinner']):
        response = requests.get(url, cookies=cookies, params=params)
    print(response.ok)

def handle_get_headers():
    url = input(ENTER_URL_TEXT)
    with console.status("Getting headers...", spinner=CONFIG['spinner']):
        response = requests.get(url, cookies=cookies, params=params)
    print(response.headers)

def handle_get_json():
    url = input(ENTER_URL_TEXT)
    response = requests.get(url, cookies=cookies, params=params)
    try:
        with console.status("Getting json...", spinner=CONFIG['spinner']):
            json_data = response.json()
            console.print(Syntax(json.dumps(json_data, indent=4), "json"))
    except ValueError:
        console.print("[red]Error: Response is not in JSON format")

def handle_check_site_availability():
    url = input(ENTER_URL_TEXT)
    with console.status("Checking availability...", spinner=CONFIG['spinner']):
        response = requests.get(url, cookies=cookies, params=params)
    if response.status_code == 200:
        print("Site is available")
    else:
        print(f"Site is not available, status code: {response.status_code}")

def handle_get_content():
    url = input(ENTER_URL_TEXT)
    with console.status("Getting content...", spinner=CONFIG['spinner']):
        response = requests.get(url, cookies=cookies, params=params)
        
    print(response.content)

def handle_set_params():
    with console.status("Reseting params...", spinner=CONFIG['spinner']):
        with open(PARAMS_FILE, 'w') as f:
            f.write("{ }")
    print("params reseted")

def handle_set_cookies():
    with console.status("Resetting cookies...", spinner=CONFIG['spinner']):
        with open(COOKIES_FILE, 'w') as f:
            f.write("{ }")
    print("cookies reseted")

def handle_set_params():
    text_json = input("Enter the json: ")
    with console.status("Writing params...", spinner=CONFIG['spinner']):
        with open(PARAMS_FILE, 'w') as f:
            f.write(text_json)
    print("params seted")

def handle_set_cookies():
    text_json = input("Enter the json: ")
    with console.status("Writing cookies...", spinner=CONFIG['spinner']):
        with open(COOKIES_FILE, 'w') as f:
            f.write(text_json)
    print("cookies seted")

def handle_get_css():
    url = input(ENTER_URL_TEXT)
    with console.status("Getting site", spinner=CONFIG['spinner']):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
    with console.status("Getting css links", spinner=CONFIG['spinner']):
        css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet')]
    with console.status("Getting inline styles", spinner=CONFIG['spinner']):
        inline_styles = [style.string for style in soup.find_all('style')]
    
    print(f"CSS files: {' '.join(css_links)}")
    print(f"\nInline styles: {' '.join(inline_styles)}")

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
            elif cmd == "10":
                handle_set_params()
            elif cmd == "11":
                handle_set_cookies()
            elif cmd == "12":
                handle_set_params()
            elif cmd == "13":
                handle_set_cookies()
            elif cmd == "14":
                handle_get_css()
            else:
                console.print("[red]Error: Invalid command")
            print("Press enter to continue...")
            input()
        except Exception as e:
            console.print(f"[red]Error: {e}")
            print("Press enter to continue...")
            input()

if __name__ == "__main__":
    clear()
    main()