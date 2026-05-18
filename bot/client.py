import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode
from bot.logging_config import logger

class BinanceFuturesClient:
    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self, api_key: str, api_secret: str):
        if not api_key or not api_secret:
            raise ValueError("API Key and API Secret must be provided.")
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        self.session.headers.update({
            "X-MBX-APIKEY": self.api_key,
            "Content-Type": "application/x-www-form-urlencoded"
        })

    def _sign_payload(self, params: dict) -> str:
        query_string = urlencode(params)
        return hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def send_signed_request(self, method: str, endpoint: str, params: dict = None) -> dict:
        if params is None:
            params = {}
            
        params["timestamp"] = int(time.time() * 1000)
        params["recvWindow"] = 5000
        
        signature = self._sign_payload(params)
        params["signature"] = signature

        url = f"{self.BASE_URL}{endpoint}"
        logger.debug(f"Sending {method} to {url} with params: {params}")

        try:
            if method.upper() == "POST":
                response = self.session.post(url, data=params, timeout=10)
            else:
                response = self.session.get(url, params=params, timeout=10)
                
            response_json = response.json()
            if response.status_code != 200:
                error_msg = response_json.get("msg", "Unknown API error")
                raise RuntimeError(f"Binance Error: {error_msg}")
                
            return response_json

        except requests.exceptions.RequestException as e:
            logger.error(f"Network error: {e}")
            raise ConnectionError(f"Network connection failed: {e}")