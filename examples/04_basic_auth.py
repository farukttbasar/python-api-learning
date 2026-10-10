import requests

# BASIC AUTH
username = input("Enter your username > ")
password = input("Enter your password > ")
r2 = requests.get('https://httpbin.org/basic-auth/faruque/apitesting', auth=(username, password))

print(r2) # [200] --> Successful / [401] --> Unauthorized