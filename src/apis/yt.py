import requests
import argparse


parser = argparse.ArgumentParser(description="Check if a  user exists.")
parser.add_argument('username', help="The facebook username to check")


args = parser.parse_args()


username = args.username
url = f'https://youtube.com/@{username}'



response = requests.get(url)

if response.status_code == 200:
    print("100")
elif response.status_code == 404:
    print("200")
elif response.status_code == 404:
    print("200")
