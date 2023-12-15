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
headers = {"accept": "application/json"}

class QuotationApiClass():

    def getMarketInfo(self,bool="false"):
        try:
            res = requests.get(server_url + f'/v1/market/all?isDetails={bool}',  headers=headers)
            print("--------- 마켓 코드 조회 ---------")
            PandasClass().showDataFrame(res.json())
            print("--------- ----------- ---------")
        except Exception as e:
            print(f"error : {str(e)}")
    
    def getTradeInfo(self,market="KRW-BTC",count=1,cursor=1,daysAgo=1):
        try:
            res = requests.get(server_url + f'/v1/trades/ticks?market={market}&count={count}&cursor={cursor}&daysAgo={daysAgo}',  headers=headers)
            print("--------- 최근 체결 내역 ---------")
            PandasClass().showDataFrame(res.json())
            print("--------- ----------- ---------")
        except Exception as e:
            print(f"error : {str(e)}")
    
    def getTickerInfo(self,market="KRW-BTC"):
        try:
            res = requests.get(server_url + f'/v1/ticker?markets={market}',  headers=headers)
            print("--------- 현재가 정보 ---------")
            PandasClass().showDataFrame(res.json())
            print("--------- ----------- ---------")
        except Exception as e:
            print(f"error : {str(e)}")
    
    def getOrderBookInfo(self, markets=["KRW-BTC"]):
        try:
            marketList = ""
            for item in markets:
                marketList += "&markets=" +item
            res = requests.get(server_url + f'/v1/orderbook?{marketList}',  headers=headers)
            print("--------- 호가 정보 조회 ---------")
            PandasClass().showDataFrame(res.json())
            print("--------- ----------- ---------")
        except Exception as e:
            print(f"error : {str(e)}")
    
    def getCandleMinute(self,unit=1,market='KRW-BTC',count=1):
        try:
            res = requests.get(server_url + f'/v1/candles/minutes/{unit}?market={market}&count={count}',  headers=headers)
            print("--------- 분(Minute) 캔들 ---------")
            PandasClass().showDataFrame(res.json())
            print("--------- ----------- ---------")
        except Exception as e:
            print(f"error : {str(e)}")
    
    def getCandleDay(self,market='KRW-BTC',count=1):
        try:
            res = requests.get(server_url + f'/v1/candles/days?market={market}&count={count}',  headers=headers)
            print("--------- 일(Day) 캔들 ---------")
            PandasClass().showDataFrame(res.json())
            print("--------- ----------- ---------")
        except Exception as e:
            print(f"error : {str(e)}")
    
    def getCandleWeek(self,market='KRW-BTC',count=1):
        try:
            res = requests.get(server_url + f'/v1/candles/weeks?market={market}&count={count}',  headers=headers)
            print("--------- 주(Week) 캔들 ---------")
            PandasClass().showDataFrame(res.json())
            print("--------- ----------- ---------")
        except Exception as e:
            print(f"error : {str(e)}")
    
    def getCandleMonth(self,market='KRW-BTC',count=1):
        try:
            res = requests.get(server_url + f'/v1/candles/months?market={market}&count={count}',  headers=headers)
            print("--------- 월(Month) 캔들 ---------")
            PandasClass().showDataFrame(res.json())
            print("--------- ----------- ---------")
        except Exception as e:
            print(f"error : {str(e)}")
    
   