import logging
from dotenv import load_dotenv
load_dotenv()
from kiteconnect import KiteConnect
import os
logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key=os.getenv("API_KEY"))

# print(kite.login_url())
# data = kite.generate_session("260nWLEW1NKrvYtLZDjcVvv5ib5vyV3S", api_secret=os.getenv("API_SECRET"))
# print(data["access_token"])




kite.set_access_token(os.getenv("ACCESS_TOKEN"))


def placeBuyOrder(symbol,quantity=1):
# Place an order
    try:
        order_id = kite.place_order(tradingsymbol=symbol,
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=quantity,
                                    variety=kite.VARIETY_AMO,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_CNC,
                                    validity=kite.VALIDITY_DAY)

        logging.info("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        logging.info("Order placement failed: {}".format(e))
          
        
        
     
def sellStockOrder(symbol,quantity=1):
    try:
        order_id = kite.place_order(tradingsymbol=symbol,
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=quantity,
                                    variety=kite.VARIETY_AMO,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_CNC,
                                    validity=kite.VALIDITY_DAY)
        logging.info("Order not placed sucessfully with the id {}".format(order_id))
    except Exception as e:
        logging.info("Order placement failed: {}".format(e.message))



        
def getAllHoldings():
    try:
       data =  kite.holdings()
       print(data)
       return data
    except Exception as e:
        return f"failed to retreive holdings error:{e}" 
getAllHoldings()




def cancelAnOrder(order_id):
    try:
        data = kite.cancel_order(kite.VARIETY_AMO,order_id)
        return f"order cancelled successfully{data}"
    except Exception as e:
        return f"falied to cancel the order error:{e}"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# cancelAnOrder(250423001989219)
# Fetch all orders
data = kite.orders()
print(type(data))
print(data)

data = kite.profile()
print(data)
# Get instruments
kite.instruments()

# # Place an mutual fund order
# kite.place_mf_order(
#     tradingsymbol="INF090I01239",
#     transaction_type=kite.TRANSACTION_TYPE_BUY,
#     amount=5000,
#     tag="mytag"
# )

# Cancel a mutual fund order
# kite.cancel_mf_order(order_id="order_id")

# Get mutual fund instruments
kite.mf_instruments()