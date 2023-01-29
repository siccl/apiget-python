import requests
import jwt
import datetime
import os
import random
from dotenv import load_dotenv

load_dotenv()

# get token
def get_token():
    # get secret key
    secret_key = os.getenv('SECRET_KEY')
    # get time
    now = datetime.datetime.utcnow()
    # generate token
    token = jwt.encode({'exp': now + datetime.timedelta(minutes=10), 'iss': os.getenv('APIKEY')}, secret_key, algorithm='HS256')
    # return token
    return token

# get url with token
def get_url():
    # gen random number
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    # get token
    token = get_token()
    # get url
    url = os.getenv('API') + "?a=" + str(a) + "&b=" + str(b)
    # return url
    return url

# get data from url
def get_data():
    # get url
    url = get_url()
    # get token
    token = get_token()
    # show token
    print(token)
    # get data
    data = requests.get(url, headers={'Authorization': 'Bearer ' + token})
    # return data
    return data

# show result 
def show_result():
    # get data
    data = get_data()
    # show result
    print(data)
    print(data.text)

# run
show_result()
