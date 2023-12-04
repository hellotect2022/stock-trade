from api.api import *
from api.api2 import *

class Main():
    def __init__(self):
        print("hello this is main")
        #Auth_class()
        #print("시세조회",Auth_class().getMarketInfo())
        

        #print("업비트에서 거래 가능한 마켓 목록",Auth_class().getMarketInfo())
        #print("최근 체결 내역",Auth_class().getTradeInfo())
        #print("요청 당시 종목의 스냅샷을 반환한다.",Auth_class().getTickerInfo())
        #print("호가 정보 조회",Auth_class().getOrderBookInfo(markets=["BTC-ETH","KRW-BTC"]))
        #print("분(Minute) 캔들",Auth_class().getCandleMinute())
        #print("일(Day) 캔들",Auth_class().getCandleDay())
        #print("주(Week) 캔들",Auth_class().getCandleWeek())
        #print("월(Month) 캔들",Auth_class().getCandleMonth())
        
        Api2_class().init()
    
if __name__ == "__main__":
    Main()
