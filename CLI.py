import argparse

from bot.client import BinanceFuturesClient
from bot.logging_config import setup_logger
from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def print_order_summary(symbol, side, order_type, quantity, price=None):
    print("\n" + "=" * 40)
    print("ORDER REQUEST SUMMARY")
    print("=" * 40)
    print(f"Symbol      : {symbol}")
    print(f"Side        : {side}")
    print(f"Order Type  : {order_type}")
    print(f"Quantity    : {quantity}")
    if price is not None:
        print(f"Price       : {price}")


def print_response_summary(response):
    print("\n" + "=" * 40)
    print("ORDER RESPONSE DETAILS")
    print("=" * 40)
    print(f"Order ID     : {response.get('orderId', 'N/A')}")
    print(f"Status       : {response.get('status', 'N/A')}")
    print(f"Executed Qty : {response.get('executedQty', 'N/A')}")
    print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")
    print(f"Symbol       : {response.get('symbol', 'N/A')}")
    print(f"Side         : {response.get('side', 'N/A')}")
    print(f"Type         : {response.get('type', 'N/A')}")


def main():
    parser = argparse.ArgumentParser(
        description="Simplified Trading Bot for Binance Futures Testnet (USDT-M)"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT, XRPUSDT, DOGEUSDT)")
    parser.add_argument("--side", required=True, help="Order side: BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity (must be > 0)")
    parser.add_argument("--price", type=float, default=None, help="Order price (required for LIMIT orders)")

    args = parser.parse_args()

    logger = setup_logger()

    print("DEBUG: cli.py started")

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print_order_summary(symbol, side, order_type, quantity, price)

        client = BinanceFuturesClient()
        order_service = OrderService(client, logger)

        response = order_service.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        print_response_summary(response)
        print("\nSUCCESS: Order placed successfully.")

    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        print(f"\nVALIDATION ERROR: {str(e)}")

    except Exception as e:
        logger.error(f"Order placement failed: {str(e)}")
        print(f"\nFAILED: {str(e)}")


if __name__ == "__main__":
    main()