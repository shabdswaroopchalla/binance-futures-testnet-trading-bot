import requests


class OrderService:
    """
    Handles order placement logic for Binance Futures Testnet via REST API.
    """

    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def place_order(self, symbol, side, order_type, quantity, price=None):
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        self.logger.info(f"Order request: {params}")

        try:
            response = self.client.post("/fapi/v1/order", params)
            self.logger.info(f"Order response: {response}")
            return response

        except requests.exceptions.HTTPError as e:
            error_text = ""
            try:
                error_text = e.response.text
            except Exception:
                error_text = str(e)

            self.logger.error(f"HTTP error from Binance API: {error_text}")
            raise Exception(f"Binance API error: {error_text}")

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Network / request error: {str(e)}")
            raise Exception(f"Network / request error: {str(e)}")

        except Exception as e:
            self.logger.exception(f"Unexpected error while placing order: {str(e)}")
            raise Exception(f"Unexpected error: {str(e)}")