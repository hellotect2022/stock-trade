import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

class Auth_class():

    def __init__(self):
        #self.test()
        print("init!")

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
            print("result",res.json())

        except Exception as e:
            print(e)
    def getMarketInfo(self,bool="false"):
        print("getMarketInfo"," -> 업비트에서 거래 가능한 마켓 목록")
        url = f"https://api.upbit.com/v1/market/all?isDetails={bool}"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        return res.json()
    
    def getTradeInfo(self,market="KRW-BTC",count=1,cursor=1,daysAgo=1):
        print("getTradeInfo"," -> 최근 체결 내역")
        url = f"https://api.upbit.com/v1/trades/ticks?market={market}&count={count}&cursor={cursor}&daysAgo={daysAgo}"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        return res.json()
    
    def getTickerInfo(self,market="KRW-BTC"):
        print("getTickerInfo"," -> 현재가 정보")
        url = f"https://api.upbit.com/v1/ticker?markets={market}"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        return res.json()
    
    def getOrderBookInfo(self, markets=["KRW-BTC"]):
        print("getOrderBookInfo"," -> 호가 정보 조회")
        marketList = ""
        for item in markets:
            marketList += "&markets=" +item
            
        url = f"https://api.upbit.com/v1/orderbook?{marketList}"
        print(url)
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        return res.json()
    
    def getCandleMinute(self,unit=1,market='KRW-BTC',count=1):
        print("getCandleMinute"," -> 분(Minute) 캔들")
        url = f"https://api.upbit.com/v1/candles/minutes/{unit}?market={market}&count={count}"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        return res.json()
    
    def getCandleDay(self,market='KRW-BTC',count=1):
        print("getCandleMinute"," -> 일(Day) 캔들")
        url = f"https://api.upbit.com/v1/candles/days?market={market}&count={count}"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        return res.json()
    
    def getCandleWeek(self,market='KRW-BTC',count=1):
        print("getCandleMinute"," -> 주(Week) 캔들")
        url = f"https://api.upbit.com/v1/candles/weeks?market={market}&count={count}"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        return res.json()
    
    
    def getCandleMonth(self,market='KRW-BTC',count=1):
        print("getCandleMinute"," -> 월(Month) 캔들")
        url = f"https://api.upbit.com/v1/candles/months?market={market}&count={count}"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers)
        return res.json()
    
   