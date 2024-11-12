import requests
import argparse


parser = argparse.ArgumentParser(description="Check if a  user exists.")
parser.add_argument('username', help="The facebook username to check")


args = parser.parse_args()


username = args.username
url = f'https://facebook.com/{username}'



response = requests.get(url)

if response.status_code == 200:
    print("10")
elif response.status_code == 302:
    print("20")
elif response.status_code == 301:
    print("20")
else:
    None
