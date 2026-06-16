STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}


def get_portfolio_input():
    portfolio = {}
    print("Available stocks and prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"  {stock}: ${price}")

    print("\nEnter stock symbol and quantity (type 'done' to finish):")
    while True:
        symbol = input("Stock symbol: ").upper().strip()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Stock not found in price list. Try again.\n")
            continue
        try:
            quantity = int(input(f"Quantity of {symbol}: "))
            if quantity < 0:
                print("Quantity cannot be negative.\n")
                continue
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} shares of {symbol}.\n")

    return portfolio


def calculate_total(portfolio):
    total = 0
    breakdown = []
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        breakdown.append((symbol, quantity, price, value))
    return total, breakdown


def save_results(breakdown, total, filename="portfolio_summary.txt"):
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("=" * 40 + "\n")
        for symbol, quantity, price, value in breakdown:
            f.write(f"{symbol}: {quantity} shares x ${price} = ${value}\n")
        f.write("=" * 40 + "\n")
        f.write(f"Total Investment: ${total}\n")
    print(f"Results saved to {filename}")


def main():
    print("=== Stock Portfolio Tracker ===\n")
    portfolio = get_portfolio_input()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total, breakdown = calculate_total(portfolio)

    print("\n--- Portfolio Summary ---")
    for symbol, quantity, price, value in breakdown:
        print(f"{symbol}: {quantity} shares x ${price} = ${value}")
    print(f"\nTotal Investment Value: ${total}")

    save = input("\nSave results to a .txt file? (y/n): ").lower().strip()
    if save == "y":
        save_results(breakdown, total)


if __name__ == "__main__":
    main()
