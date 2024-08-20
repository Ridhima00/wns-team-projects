import requests
from bs4 import BeautifulSoup
import re


# Path to the hosts file (Windows)
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

# Path to the hosts file (Linux/Mac)
# hosts_path = "/etc/hosts"

# Redirect to localhost
redirect = "127.0.0.1"

# List of websites to block
website_list = []

def get_user_input():
    while True:
        website = input("Enter a website to block (or 'done' to finish): ")
        if website.lower() == 'done':
            break
        if not website.startswith("www."):
            website = "www." + website
        website_list.append(website)
    print(f"Websites to block: {website_list}")

def scrape_and_check(url, pattern):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text()
        if re.search(pattern, content, re.IGNORECASE):
            return True
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
    return False

def block_based_on_pattern(pattern):
    websites_to_check = ["example.com", "somesite.com"]  # Add websites to check
    for website in websites_to_check:
        if scrape_and_check("http://" + website, pattern):
            if website not in website_list:
                website_list.append(website)
    print(f"Websites matching pattern '{pattern}': {website_list}")
    block_websites()

def block_websites():
    with open(hosts_path, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website not in content:
                file.write(redirect + " " + website + "\n")
    print("Websites blocked.")

def unblock_websites():
    with open(hosts_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()
    print("Websites unblocked.")

if __name__ == "__main__":
    pattern = input("Enter a pattern to block websites: ")
    block_based_on_pattern(pattern)
    get_user_input()
    block_websites()
    # To unblock websites, uncomment the following line
    # unblock_websites()

