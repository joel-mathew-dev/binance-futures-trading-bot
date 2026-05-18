import os
import sys
import argparse
from bot.validators import validate_inputs
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.logging_config import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures CLI Trading Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)
    except ValueError as val_err:
        logger.error(f"Validation Error: {val_err}")
        sys.exit(1)

    api_key = os.getenv("BINANCE_TESTNET_API_KEY")
    api_secret = os.getenv("BINANCE_TESTNET_API_SECRET")

    if not api_key or not api_secret:
        logger.error("API credentials missing from environment variables!")
        sys.exit(1)

    try:
        client = BinanceFuturesClient(api_key, api_secret)
        manager = OrderManager(client)
        
        response = manager.create_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n" + "="*40)
        print("🎉 SUCCESS: ORDER PLACED")
        print("="*40)
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice', '0.0')}")
        print("="*40 + "\n")

    except Exception as run_err:
        print(f"\n❌ ERROR: {run_err}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()