import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

class Auth_class():

    def __init__(self):
        res = self.test()
        print(f"res :{res}")

    def test(self):
        try:
            # access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
            #secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
            #server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']
            access_key = ''
            secret_key = ''
            server_url = 'https://api.upbit.com'
            print("access_key:",access_key)
            print("secret_key:",secret_key)
            print("server_url:",server_url)

            payload = {
                'access_key': access_key,
                'nonce': str(uuid.uuid4()),
            }

            jwt_token = jwt.encode(payload, secret_key)
            print(f"jwt_token : {jwt_token}")
            authorization = 'Bearer {}'.format(jwt_token)
            headers = {
                'Authorization': authorization,
            }

            res = requests.get(server_url + '/v1/accounts',  headers=headers)
            res.json()

        except Exception as e:
            print(e)