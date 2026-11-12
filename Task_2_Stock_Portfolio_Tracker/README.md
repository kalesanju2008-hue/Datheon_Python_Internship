# Task 2 – Stock Portfolio Performance Tracker

## Description
A Python-based application that helps users track and analyse their stock investments. Users can enter stock ticker symbols, purchase prices, share quantities, and current stock prices.

The application calculates individual stock performance and overall portfolio performance, including investment value, market value, profit or loss, and percentage returns.

## Features
- Add multiple stock holdings.
- Enter stock ticker symbols, buying prices, and share quantities.
- Fetch the latest available stock prices using Yahoo Finance.
- Manually enter current prices if live prices are unavailable.
- Calculate total investment and current market value.
- Calculate individual and overall profit/loss.
- Calculate percentage returns.
- Save holding details and portfolio summaries in a CSV file.
- Validate user input.

## Technologies Used
- Python
- CSV Module
- Dictionaries
- Functions and Loops
- File Handling
- Pathlib and Datetime
- yfinance (optional, for live stock prices)

## Project Files
- `portfolio.py` – Main Python application.
- `portfolio_summary.csv` – Stores portfolio performance records.
- `README.md` – Project documentation.

## Installation

1. Install Python 3.
2. Open the terminal in the project folder.
3. (Optional) Install yfinance for live stock prices:

   `python -m pip install yfinance`

## How to Run

Run the following command:

`python portfolio.py`

Follow the instructions to enter your stock details. Press Enter at the ticker prompt when you have finished adding stocks.

## Output
The application displays:
- Individual stock investment details.
- Current market value.
- Profit or loss.
- Percentage returns.
- Overall portfolio performance.

The results are automatically saved in `portfolio_summary.csv`.

## Note
Live stock prices require an internet connection and the optional yfinance package. If live prices are unavailable, users can enter current prices manually.
