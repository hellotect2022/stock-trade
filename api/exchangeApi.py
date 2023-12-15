import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote
from key.KeyClass import KeyClass
from ui.PandasClass import *

access_key = KeyClass().getAccessKey()
secret_key = KeyClass().getSecretKey()
server_url = KeyClass().getServerUrl()
payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}
jwt_token = jwt.encode(payload, secret_key).decode('utf-8')
authorization = 'Bearer {}'.format(jwt_token)
headers = {
    'Authorization': authorization,
}

class AccountClass():
    # 내 자산 현황 가져오기
    def getMyAccounts(self):
        try:
            res = requests.get(server_url + '/v1/accounts',  headers=headers)
            res.json()
            print("--------- 내 자산 현황 ---------")
            PandasClass().showDataFrame(res.json())
            print("--------- ----------- ---------")

        except Exception as e:
            print(e)

class OrderClass():
    # 주문 가능 정보

    def setRequest(self,params):
        query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")
        m = hashlib.sha512()
        m.update(query_string)
        query_hash = m.hexdigest()
        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
            'query_hash': query_hash,
            'query_hash_alg': 'SHA512'
        }
        jwt_token = jwt.encode(payload, secret_key).decode('utf-8')
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
            'Authorization': authorization,
        }
        return headers

    def getOrderChance(self,params={'market': 'KRW-BTC'}):
        try:
            headers = self.setRequest(params)
            res = requests.get(server_url + '/v1/orders/chance', params=params, headers=headers)
            res.json()
            print("--------- 주문 가능 정보 ---------")
            PandasClass().showDataFrame(res.json())
            print("---------  -----------  ---------")
        except Exception as e:
            print(e)

    def getOrder(self,params={'uuid': '01004020-0400-0000-0200-001101010000'}):
        try:
            headers = self.setRequest(params)
            res = requests.get(server_url + '/v1/order', params=params, headers=headers)
            res.json()
            print("--------- 개별 주문 조회 ---------")
            PandasClass().showDataFrame(res.json())
            print("---------  -----------  ---------")
        except Exception as e:
            print(e)

    def getOrderList(self,params={'states[]': ['done', 'cancel']}, filter=None):
        try:
            headers = self.setRequest(params)
            res = requests.get(server_url + '/v1/orders', params=params, headers=headers)
            res.json()
            print("--------- 주문 리스트 조회 ---------")
            PandasClass().showDataFrame(res.json(), filter)
            print("---------  -----------   ---------")
        except Exception as e:
            print(e)

    def deleteOrderList(self,params={'uuid': '01004020-0400-0000-0200-001101010000'}):
        try:
            headers = self.setRequest(params)
            res = requests.delete(server_url + '/v1/order', params=params, headers=headers)
            res.json()
            print("--------- 주문 취소 접수 ----------")
            PandasClass().showDataFrame(res.json())
            print("---------  -----------   ---------")
        except Exception as e:
            print(e)
    
    def postOrder(self,params = {'market': 'KRW-BTC', 'side': 'bid', 'ord_type': 'limit', 'price': '100.0','volume': '0.01'}):
        try:
            headers = self.setRequest(params)
            res = requests.post(server_url + '/v1/orders', params=params, headers=headers)
            res.json()
            print("--------- 주문하기 ----------")
            print(res.json())
            #PandasClass().showDataFrame(res.json())
            print("---------  -----------------")
        except Exception as e:
            print(f"error : {str(e)}")

class WalletClass():
    # 입출금 현황
    def getMyWalletStatus(self):
        try:
            res = requests.get(server_url + '/v1/status/wallet',  headers=headers)
            res.json()
            print("---------  입출금 현황 ---------")
            PandasClass().showDataFrame(res.json())
            print("--------- ----------- ---------")

        except Exception as e:
            print(e)
    
    
   