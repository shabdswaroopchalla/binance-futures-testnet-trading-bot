# Binance Futures Testnet Trading Bot

A simplified Python trading bot built for Binance Futures Testnet (USDT-M).  
This CLI-based application supports placing MARKET and LIMIT orders with proper input validation, structured code organization, logging, and error handling.

---

## Features

- Place **MARKET** and **LIMIT** orders on **Binance Futures Testnet (USDT-M)**
- Supports both order sides:
  - **BUY**
  - **SELL**
- CLI input using **argparse**
- Input validation for:
  - symbol
  - side
  - order type
  - quantity
  - price (required for LIMIT)
- Clean code structure:
  - API/client layer
  - order service layer
  - validators
  - CLI layer
- Logs:
  - API requests
  - API responses
  - validation errors
  - runtime exceptions
- Clear console output:
  - order request summary
  - order response details
  - success/failure message

---

## Project Structure

trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── README.md
├── requirements.txt
├── .env
└── .gitignore

---

## Setup Instructions

### 1) Clone the repository

```bash
git clone <your_repo_url>
cd trading_botgit init