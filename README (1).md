# Binance Futures CLI Trading Bot

A modular Python command-line bot that places orders on the **Binance Futures Testnet**. It connects to the exchange API, validates every input before sending it, signs each request securely, and writes structured logs of everything it does.

> **Testnet only.** This project uses Binance's demo environment with test funds. No real money is involved.

## Features

- Places **MARKET** and **LIMIT** orders
- Validates all user input before any request is sent
- Signs API requests with **HMAC-SHA256**
- Logs to both the **console** and a **log file**
- Layered, modular code that is easy to read and extend

## Project Structure

```
binance-futures-trading-bot/
├── cli.py               # Entry point: handles terminal commands and arguments
├── requirements.txt     # Third-party dependencies
├── .gitignore           # Keeps logs and secrets out of the repo
└── bot/
    ├── __init__.py      # Makes bot/ a Python package
    ├── client.py        # API sessions, payloads, HMAC-SHA256 request signing
    ├── orders.py        # Builds order payloads and places orders
    ├── validators.py    # Sanitizes and validates inputs before sending
    └── logging_config.py  # Dual logging: console stream + file
```

## How It Works

```
cli.py  ->  validators.py  ->  orders.py  ->  client.py  ->  Binance Futures Testnet
 (input)     (check input)     (build order)   (sign + send)
                                   |
                            logging_config.py (logs every step)
```

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/joel-mathew-dev/binance-futures-trading-bot.git
cd binance-futures-trading-bot
```

**2. Install dependencies** (Python 3 required)

```bash
pip install -r requirements.txt
```

**3. Get Testnet API keys**

Create a Binance Futures Testnet account and generate an API key and secret from the testnet dashboard.

**4. Add your keys**

The bot reads your keys from environment variables, so they are never stored in the code. Set them before running:

```bash
# Linux / macOS
export BINANCE_TESTNET_API_KEY="your_testnet_api_key"
export BINANCE_TESTNET_API_SECRET="your_testnet_api_secret"

# Windows (PowerShell)
$env:BINANCE_TESTNET_API_KEY="your_testnet_api_key"
$env:BINANCE_TESTNET_API_SECRET="your_testnet_api_secret"
```

If the keys are missing, the bot logs an error and exits. Never commit your keys to GitHub.

## Usage

| Option | Required | Description |
| --- | --- | --- |
| `--symbol` | Yes | Trading pair, e.g. `BTCUSDT` |
| `--side` | Yes | `BUY` or `SELL` |
| `--type` | Yes | `MARKET` or `LIMIT` |
| `--quantity` | Yes | Order quantity (number) |
| `--price` | For LIMIT orders | Limit price (number) |

**Place a MARKET order**

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Place a LIMIT order**

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 100000
```

**See all options**

```bash
python cli.py --help
```

Adjust the quantity and price to values the testnet accepts for your symbol.

## Example Output

After a successful order, the bot prints a summary like this (values below are examples):

```
========================================
SUCCESS: ORDER PLACED
========================================
Order ID     : 123456789
Status       : NEW
Executed Qty : 0.000
Avg Price    : 0.0
========================================
```

If something goes wrong (invalid input, missing keys, or an API error), the bot logs the problem and exits with an error message.

## Logging

Every request, response and error is logged to the console and to a log file. The log file is created automatically when the bot runs and is excluded from the repo through `.gitignore`.

## Possible Improvements

- Add a trading strategy (for example, a moving-average crossover)
- Support more order types (stop-limit, stop-market)
- Add unit tests for the validators

## Tech

Python 3, Binance Futures Testnet REST API, HMAC-SHA256, argparse-style CLI, logging

## Disclaimer

This is a learning project for demo trading. It is not financial advice.
