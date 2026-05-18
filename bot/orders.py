from bot.client import BinanceFuturesClient
from bot.logging_config import logger

class OrderManager:
    def __init__(self, client: BinanceFuturesClient):
        self.client = client

    def create_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None) -> dict:
        payload = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": str(quantity),
        }
        
        if order_type == "LIMIT":
            payload["price"] = str(price)
            payload["timeInForce"] = "GTC"

        logger.info(f"Placing Order -> {side} {quantity} {symbol} ({order_type})")
        return self.client.send_signed_request("POST", "/fapi/v1/order", payload)