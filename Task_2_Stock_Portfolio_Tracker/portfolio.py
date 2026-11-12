
"""
Stock Portfolio Performance Tracker
-----------------------------------
Enter ticker symbols, purchase prices, and share quantities. The program tries
to fetch the latest price with yfinance. If yfinance is unavailable or a quote
cannot be fetched, it asks for the current price manually.

Each run appends holding-level results and a portfolio total to
portfolio_summary.csv.

Optional live-price dependency:
    python -m pip install yfinance
"""

import csv
from datetime import datetime
from pathlib import Path

OUTPUT_FILE = Path(__file__).with_name("portfolio_summary.csv")

FIELDNAMES = [
    "record_type",
    "timestamp",
    "ticker",
    "shares",
    "buy_price",
    "current_price",
    "invested_value",
    "market_value",
    "profit_loss",
    "return_pct",
]


def get_live_price(ticker):
    """Return the latest available market price, or None if unavailable."""
    try:
        import yfinance as yf
        info = yf.Ticker(ticker).fast_info
        price = info.get("lastPrice")
        if price is None:
            price = info.get("regularMarketPrice")
        if price is not None and float(price) > 0:
            return float(price)
    except Exception:
        pass
    return None


def ask_positive_number(prompt):
    """Read a positive number from the user."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0:
                return value
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def ask_portfolio():
    """Collect portfolio positions and return them in a dictionary."""
    positions = {}
    while True:
        ticker = input("\nEnter stock ticker (or press Enter to finish): ").strip().upper()
        if not ticker:
            break

        if ticker in positions:
            print("That ticker is already in your portfolio. Enter it only once.")
            continue

        buy_price = ask_positive_number(f"Enter buy price for {ticker}: ")
        shares = ask_positive_number(f"Enter number of shares for {ticker}: ")

        current_price = get_live_price(ticker)
        if current_price is not None:
            print(f"Latest available price for {ticker}: {current_price:.2f}")
            use_live = input("Use this price? [Y/n]: ").strip().lower()
            if use_live in ("", "y", "yes"):
                price = current_price
            else:
                price = ask_positive_number(f"Enter current price for {ticker}: ")
        else:
            print("Live price unavailable. You can enter the current price manually.")
            price = ask_positive_number(f"Enter current price for {ticker}: ")

        positions[ticker] = {
            "buy_price": buy_price,
            "shares": shares,
            "current_price": price,
        }

    return positions


def calculate_results(positions):
    """Calculate holding-level performance and portfolio totals."""
    results = []
    total_invested = 0.0
    total_market_value = 0.0

    for ticker, position in positions.items():
        invested = position["buy_price"] * position["shares"]
        market_value = position["current_price"] * position["shares"]
        profit_loss = market_value - invested
        return_pct = (profit_loss / invested) * 100 if invested else 0.0

        results.append({
            "ticker": ticker,
            "shares": position["shares"],
            "buy_price": position["buy_price"],
            "current_price": position["current_price"],
            "invested_value": invested,
            "market_value": market_value,
            "profit_loss": profit_loss,
            "return_pct": return_pct,
        })
        total_invested += invested
        total_market_value += market_value

    total_profit_loss = total_market_value - total_invested
    total_return_pct = (
        (total_profit_loss / total_invested) * 100 if total_invested else 0.0
    )

    totals = {
        "invested_value": total_invested,
        "market_value": total_market_value,
        "profit_loss": total_profit_loss,
        "return_pct": total_return_pct,
    }
    return results, totals


def print_report(results, totals):
    """Display a readable portfolio report in the console."""
    print("\n" + "=" * 88)
    print("STOCK PORTFOLIO PERFORMANCE")
    print("=" * 88)
    print(
        f"{'Ticker':<10}{'Shares':>10}{'Buy Price':>13}{'Current':>13}"
        f"{'Invested':>14}{'Market Value':>16}{'P/L %':>10}"
    )
    print("-" * 88)

    for item in results:
        print(
            f"{item['ticker']:<10}{item['shares']:>10.2f}"
            f"{item['buy_price']:>13.2f}{item['current_price']:>13.2f}"
            f"{item['invested_value']:>14.2f}{item['market_value']:>16.2f}"
            f"{item['return_pct']:>9.2f}%"
        )

    print("-" * 88)
    print(f"{'TOTAL':<10}{'':>10}{'':>13}{'':>13}"
          f"{totals['invested_value']:>14.2f}"
          f"{totals['market_value']:>16.2f}"
          f"{totals['return_pct']:>9.2f}%")
    print(f"Total Profit / Loss: {totals['profit_loss']:+.2f}")
    print("=" * 88)


def save_to_csv(results, totals):
    """Append this run's holding details and portfolio summary to the CSV."""
    file_exists = OUTPUT_FILE.exists() and OUTPUT_FILE.stat().st_size > 0
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")

    with OUTPUT_FILE.open("a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        if not file_exists:
            writer.writeheader()

        for item in results:
            writer.writerow({
                "record_type": "HOLDING",
                "timestamp": timestamp,
                **item,
            })

        writer.writerow({
            "record_type": "PORTFOLIO_TOTAL",
            "timestamp": timestamp,
            "ticker": "ALL",
            "shares": "",
            "buy_price": "",
            "current_price": "",
            **totals,
        })


def main():
    print("STOCK PORTFOLIO PERFORMANCE TRACKER")
    print("Enter your holdings. Press Enter at the ticker prompt when finished.")

    positions = ask_portfolio()
    if not positions:
        print("\nNo holdings entered. Nothing to calculate.")
        return

    results, totals = calculate_results(positions)
    print_report(results, totals)
    save_to_csv(results, totals)
    print(f"\nPerformance log saved to: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()
