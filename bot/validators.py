def validate_symbol(symbol: str) -> str:
    if not symbol:
        raise ValueError("Symbol is required.")

    symbol = symbol.upper().strip()

    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must be a USDT-M futures pair like BTCUSDT or XRPUSDT.")

    return symbol


def validate_side(side: str) -> str:
    if not side:
        raise ValueError("Side is required.")

    side = side.upper().strip()

    if side not in {"BUY", "SELL"}:
        raise ValueError("Side must be either BUY or SELL.")

    return side


def validate_order_type(order_type: str) -> str:
    if not order_type:
        raise ValueError("Order type is required.")

    order_type = order_type.upper().strip()

    if order_type not in {"MARKET", "LIMIT"}:
        raise ValueError("Order type must be either MARKET or LIMIT.")

    return order_type


def validate_quantity(quantity: float) -> float:
    if quantity is None:
        raise ValueError("Quantity is required.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    return quantity


def validate_price(price, order_type: str):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        if price <= 0:
            raise ValueError("Price must be greater than 0 for LIMIT orders.")

    return price