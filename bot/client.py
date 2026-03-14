import os
import time
import hmac
import hashlib
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv


class BinanceFuturesClient:
    """
    Simple REST client for Binance Futures Testnet (USDT-M).
    """

    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self):
        load_dotenv()

        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            raise ValueError(
                "Missing Binance API credentials. Please set BINANCE_API_KEY and BINANCE_API_SECRET in .env"
            )

        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key
        })

    def _sign_params(self, params: dict) -> dict:
        """
        Add timestamp + signature to params.
        """
        params["timestamp"] = int(time.time() * 1000)
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def post(self, path: str, params: dict):
        """
        Signed POST request to Binance Futures Testnet.
        """
        signed_params = self._sign_params(params)
        url = f"{self.BASE_URL}{path}"

        response = self.session.post(url, params=signed_params, timeout=15)

        # Raise HTTP error if status code is bad
        response.raise_for_status()

        return response.json()