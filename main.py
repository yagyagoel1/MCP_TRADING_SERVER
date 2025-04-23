from mcp.server.fastmcp import FastMCP
from .trade import (placeBuyOrder,sellStockOrder,getAllHoldings,cancelAnOrder)
# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def placeBuyStockOrder(quantity:int,symbol:str):
    """Place a order on zerodha of the defined quantity for the symbol"""
    try:
        data = placeBuyOrder(symbol,quantity)
        return f"order buy placed successfullt {data}"
    except Exception as e:
        return f"falied to place order error:{e}"
    
@mcp.tool()
def sellStocks(quantity:int,symbol:str):
    """Sell the stock on zerodha"""
    try:
        data = sellStockOrder(symbol,quantity)
        return f"order sell placed successfullt {data}"
    except Exception as e:
        return f"falied to place order error:{e}"
    
@mcp.tool()
def getHoldings():
    """this is to fetch all the holdings for the user in zerodha"""
    try:
        data = getAllHoldings()
        return f"Holdings fetched successfully holdings:{data}"
    except Exception as e:
        return f"falied to fetch holdings error:{e}"
    
@mcp.tool()
def cancelOrder(order_id:int):
    """Cancel all the order with the specified order id"""
    try:
        data = cancelAnOrder(order_id)
        
        return f"Cancelled the holdings successfully {data}"
    except Exception as e:
        return f"failed to cancel the order {e}"