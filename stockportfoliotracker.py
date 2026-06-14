stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", ", ".join(stock_prices.keys()))

n = int(input("How many different stocks do you own? "))

for i in range(n):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"Investment in {stock}: ${investment}")
    else:
        print("Stock not found in portfolio.")

print("\nTotal Investment Value: $", total_investment)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Portfolio saved to portfolio.txt")