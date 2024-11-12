import os
import subprocess
import json
import time

func = "./src/func/"
apis = "./src/apis/"
config = "./src/config/"
plats = {}


with open(f'{config}config.json', 'r') as config_file:
    config = json.load(config_file)

twitter_bearer_token = config['twitter']['bearer_token']

logo = """ 

________         .__        __      _________             .__       .__          
\_____  \   _____|__| _____/  |_   /   _____/ ____   ____ |__|____  |  |   ______
 /   |   \ /  ___/  |/    \   __\  \_____  \ /  _ \_/ ___\|  \__  \ |  |  /  ___/
/    |    \\___ \|  |   |  \  |    /        (  <_> )  \___|  |/ __ \|  |__\___ \ 
\_______  /____  >__|___|  /__|   /_______  /\____/ \___  >__(____  /____/____  >
        \/     \/        \/               \/            \/        \/          \/ 
                            By @znlv on github
"""

choice = """ 
 
 ________         .__        __      _________             .__       .__          
 \_____  \   _____|__| _____/  |_   /   _____/ ____   ____ |__|____  |  |   ______
  /   |   \ /  ___/  |/    \   __\  \_____  \ /  _ \_/ ___\|  \__  \ |  |  /  ___/
 /    |    \\___ \|  |   |  \  |    /        (  <_> )  \___|  |/ __ \|  |__\___ \ 
 \_______  /____  >__|___|  /__|   /_______  /\____/ \___  >__(____  /____/____  >
         \/     \/        \/               \/            \/        \/          \/ 
                             By @znlv on github

                            1) An Account Finder
                            2) Twitter Data Finder
 """

def clear():
    if os.name == 'nt': 
        subprocess.run("cls", shell=True)
    else:    
        subprocess.run("clear", shell=True)

def slowprint(txt, speed, color):
    subprocess.run(["python", f"{func}/slow.py", txt, "--delay", speed, "--color", color], check=True)

def check_status_code(status_code, user, platform):
    if platform == 'twitter':
        if status_code == 1:
            return f"Twitter Account found under username: {user}"
            plat[platform]
        elif status_code == 2:
            return None
        elif status_code == 3:
            return None
        else:
            return "Invalid status code for Twitter."

    elif platform == 'facebook':
        if status_code == 10:
            return f"Facebook Account found under username: {user}"
            plat[platform]
        elif status_code == 20:
            return None
        else:
            return "Invalid status code for Facebook."
        
    elif platform == 'yt':
        if status_code == 100:
            return f"YouTube Account found under username: {user}"
            plat[platform]
        elif status_code == 200:
            return None

    elif platform == 'instagram':
        if status_code == 30:
            return f"Instagram Account found under username: {user}"
            plat[platform]
        elif status_code == 40:
            return None
        else:
            return "Invalid status code for Instagram."

    else:
        return "Invalid platform."


def twitter(twitter_bearer_token, user, apis):
    result = subprocess.run(
        ["python", f"{apis}/x.py", twitter_bearer_token, user],
        check=True,
        capture_output=True,
        text=True 
    )
    
    twitter_status = int(result.stdout.strip())  
    response = check_status_code(twitter_status, user,platform="twitter")
    
    if response is not None:
        print(response)

def fb(user, apis):
    result = subprocess.run(
        ["python", f"{apis}/fb.py", user],
        check=True,
        capture_output=True,
        text=True 
    )
    
    facebook_status = int(result.stdout.strip())  
    response = check_status_code(facebook_status, user, platform="facebook")
    
    if response is not None:
        print(response)

def yt(user, apis):
    result = subprocess.run(
        ["python", f"{apis}/yt.py", user],
        check=True,
        capture_output=True,
        text=True 
    )
    
    facebook_status = int(result.stdout.strip())  
    response = check_status_code(facebook_status, user, platform="yt")
    
    if response is not None:
        print(response)



def acc():
 clear()
 
 logo = """ 
 
 ________         .__        __      _________             .__       .__          
 \_____  \   _____|__| _____/  |_   /   _____/ ____   ____ |__|____  |  |   ______
  /   |   \ /  ___/  |/    \   __\  \_____  \ /  _ \_/ ___\|  \__  \ |  |  /  ___/
 /    |    \\___ \|  |   |  \  |    /        (  <_> )  \___|  |/ __ \|  |__\___ \ 
 \_______  /____  >__|___|  /__|   /_______  /\____/ \___  >__(____  /____/____  >
         \/     \/        \/               \/            \/        \/          \/ 
                             By @znlv on github
 """

 slowprint(logo, speed='0.001', color='red')
 user = input('Put the username you wanna find the accs of: ')
 clear()
 slowprint(logo, speed='0.001', color='red')
 twitter(twitter_bearer_token, user,apis)
 fb(user,apis)
 yt(user,apis)
 slowprint("That where the results...", speed="0.05", color="white")
 time.sleep(3)
 exit()

def twitterprofile():
    print("nigger")


def choicescreen():
 slowprint(choice, speed='0.001', color='red')
 choic = int(input("Choose what you want to use: "))
  
 if choic == 1:
      acc()
 elif choic == 2:
      twitterprofile()
 else:
      slowprint("Unkown Result, Please enter 1 or 2", speed="0.05", color="white")
      clear()
      slowprint(choice, speed='0.001', color='red')


choicescreen()