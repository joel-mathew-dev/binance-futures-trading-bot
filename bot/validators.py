def validate_inputs(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    if not symbol.isalnum() or not symbol.isupper():
        raise ValueError(f"Invalid symbol '{symbol}'. Must be uppercase (e.g., BTCUSDT).")
        
    if side not in ["BUY", "SELL"]:
        raise ValueError(f"Invalid side '{side}'. Must be either 'BUY' or 'SELL'.")
        
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError(f"Invalid order type '{order_type}'. Must be 'MARKET' or 'LIMIT'.")
        
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
        
    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("Price is required and must be greater than 0 for LIMIT orders.")