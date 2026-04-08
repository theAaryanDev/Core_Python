#Lecture 22 : Handling API in python
#Supporting Lecture 22.1 : What is an API in Hindi | Link → https://www.youtube.com/watch?v=0PaWV3wIfkM

#freeapi.app / api.freeapi.app → have many APIs to practice → built by Hitesh Sir
# jsonformatter.org → site to visulaize and convert api requests into json 
#for first time → pip/pip3 install requests → requests: is a python library for handling APIs
#2nd step: import requests → to use requests library.
#Assignment: read about POST, PUT in API chai aur code
#Assignment: try 2 API handling with yourself.
#to activate virtual environment → & c:\Aryan\TheAryanDev\Python\.venv\Scripts\Activate.ps1
#to deactivate virtual environment → deactivate

import requests

def generate_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url) #NOTE: response come in string of object format
    response_in_json = response.json() #NOTE: response here is converted from str to json / python dictionary

    # if response_in_json['success']: #check if response_in_json['success'] == True | Method 1
    if response_in_json.get('success'): #check if status code is 200 OK | Method 2
        username = response_in_json['data']['login']['username']
        password = response_in_json['data']['login']['password']
        country = response_in_json['data']['location']['country']
        return username, password, country
    else:
        raise Exception("Failed to call API") #raise → to raise something (generally exceptions) | Exception → your custumized exception messsage to user

def main():
    try:
        username, password, country = generate_random_user()
        print(f"Username: {username} \nPass: {password} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

#Assignment: try 2 API handling with yourself.
#resources for APIs handling Practice: 1. https://freeapi.app/ , 2. https://jsonformatter.org/