# CodeAlpha Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190,
    "TSLA": 250
}

portfolio = {}
total_value = 0

print("Welcome to Stock Portfolio Tracker!")

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not found. Please choose from:")
        print(", ".join(stocks.keys()))
        continue

    quantity = int(input("Enter quantity: "))

    portfolio[stock] = quantity

print("\nYour Portfolio:")

for stock, quantity in portfolio.items():
    value = stocks[stock] * quantity
    total_value += value
    print(stock, "-", quantity, "shares =", "$", value)

print("\nTotal Portfolio Value: $", total_value)
