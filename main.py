import requests
import jwt
import datetime
import os
import random
from dotenv import load_dotenv

load_dotenv()

# get token
def get_token():
    secret_key = os.getenv('SECRET_KEY')
    now = datetime.datetime.utcnow()
    token = jwt.encode(
        {
            'exp': now + datetime.timedelta(minutes=10), 
            'iss': os.getenv('APIKEY'),
            'nbf': now
            # "jti" (JWT ID) Claim
            # "iat" (Issued At) Claim
            # "aud" (Audience) Claim
            # "sub" (Subject) Claim
            # "exp" (Expiration Time) Claim
            # "nbf" (Not Before) Claim
            # "iss" (Issuer) Claim
            # "prn" (Principal) Claim
            # "cty" (Content Type) Claim
            # "kid" (Key ID) Claim
         },
         secret_key, 
         algorithm='HS256'
        # "alg" (Algorithm) Claim
        # "typ" (Type) Claim : "JWT"
    )
    return token

# get url with token
def get_url():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    token = get_token()
    url = os.getenv('API') + "?a=" + str(a) + "&b=" + str(b)
    return url

# get data from url
def get_data():
    url = get_url()
    token = get_token()
    print(token)
    data = requests.get(url, headers={'Authorization': 'Bearer ' + token})
    return data

# show result 
def show_result():
    data = get_data()
    print(data)
    print(data.text)

# run
show_result()