from api.exchangeApi import *
from api.quotationApi import *

class Main():
    def __init__(self):
        print("Main Program is start!!")

        #price=5000
        #num = 1
        #BTC_KRW = 58405000
        #print(1/BTC_KRW*100)

        #OrderClass().postOrder({'market': 'KRW-BTC', 'side': 'bid', 'ord_type': 'price', 'price': '5000', 'volume': ''})
        #AccountClass().getMyAccounts()
        #WalletClass().getMyWalletStatus()
        #OrderClass().getOrderChance({'market': 'KRW-BTC'})
        #OrderClass().getOrder({'uuid': '5e16204c-d399-42b7-a923-bf6f6c83ebb4'})
        #OrderClass().getOrderList({'states[]': ['done', 'cancel']},filter={'column':'created_at', 'value':'2023-12-15T'})
        #OrderClass().getOrderList({'states[]': ['wait', 'watch']},filter={'column':'created_at', 'value':'2023-12-15T'})
        #OrderClass().deleteOrderList({'uuid': '01004020-0400-0000-0200-001101010000'})
        
        #Quotation Api
        QuotationApiClass().getMarketInfo(bool="false")
        QuotationApiClass().getTradeInfo(market="KRW-BTC",count=10,cursor=10,daysAgo=7)
        QuotationApiClass().getTickerInfo(market="KRW-BTC")
        QuotationApiClass().getOrderBookInfo(markets=["KRW-BTC"])

        #QuotationApiClass().getCandleMinute(unit=1,market='KRW-BTC',count=10)
        #uotationApiClass().getCandleDay(market='KRW-BTC',count=1)
        #QuotationApiClass().getCandleWeek(market='KRW-BTC',count=1)
        #QuotationApiClass().getCandleMonth(market='KRW-BTC',count=1)
        

        #print("업비트에서 거래 가능한 마켓 목록",Auth_class().getMarketInfo())
        #print("최근 체결 내역",Auth_class().getTradeInfo())
        #print("요청 당시 종목의 스냅샷을 반환한다.",Auth_class().getTickerInfo())
        #print("호가 정보 조회",Auth_class().getOrderBookInfo(markets=["BTC-ETH","KRW-BTC"]))
        #print("분(Minute) 캔들",Auth_class().getCandleMinute())
        #print("일(Day) 캔들",Auth_class().getCandleDay())
        #print("주(Week) 캔들",Auth_class().getCandleWeek())
        #print("월(Month) 캔들",Auth_class().getCandleMonth())
        
        #Api2_class().init()
    
if __name__ == "__main__":
    Main()
