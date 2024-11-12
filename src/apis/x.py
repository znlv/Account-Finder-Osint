import requests
import argparse


parser = argparse.ArgumentParser(description="Check if a Twitter user exists.")
parser.add_argument('bearer_token', help="The Bearer Token for Twitter API authentication")
parser.add_argument('username', help="The Twitter username to check")


args = parser.parse_args()

BEARER_TOKEN = args.bearer_token
username = args.username
url = f'https://api.twitter.com/2/users/by/username/{username}'

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print("1")
elif response.status_code == 404:
    print("2")
elif response.status_code == 492:
    None