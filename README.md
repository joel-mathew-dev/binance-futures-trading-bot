\# Binance Futures CLI Trading Bot



A modular, layered Python command-line interface (CLI) trading bot built for the Binance Futures Testnet. This application securely connects to the exchange matching engine, validates user inputs, and executes both MARKET and LIMIT orders while generating structured runtime logs.



\## 📁 Project Structure

\* `cli.py` - The entry point of the application; handles terminal commands and arguments.

\* `requirements.txt` - Lists required third-party dependencies.

\* `bot/` - Core application package directory.

&#x20; \* `\_\_init\_\_.py` - Initializes the bot folder as a Python package.

&#x20; \* `client.py` - Manages API sessions, payloads, and HMAC-SHA256 signature cryptographic signing.

&#x20; \* `orders.py` - Formats transaction payloads and handles order placement.

&#x20; \* `validators.py` - Sanitizes and validates user inputs before network transmission.

&#x20; \* `logging\_config.py` - Configures dual-handler logging (Console stream + File storage).



\---



\## 🛠️ Installation \& Setup



1\. \*\*Install Dependencies\*\*

&#x20;  Ensure you have Python 3 installed, then run:

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

