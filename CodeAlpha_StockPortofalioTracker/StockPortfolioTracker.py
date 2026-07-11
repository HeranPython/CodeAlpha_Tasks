stock_prices = {"AAPL": 180,"TSLA": 250,"AMZN": 140,"GOOGL": 135,"MSFT": 330}

portfolio = {}

print("Enter number of shares you own (0 if none):\n")


for stock in stock_prices:
    shares = int(input(f"{stock}: "))
    portfolio[stock] = shares


total_investment = 0
report_lines = []

print("\n--- Portfolio Summary ---")

for stock in stock_prices:
    shares = portfolio[stock]
    price = stock_prices[stock]
    value = shares * price
    total_investment += value

    line = f"{stock}: {shares} shares × {price} = {value}"
    print(line)
    report_lines.append(line)


print("\nTOTAL INVESTMENT VALUE:", total_investment)
report_lines.append(f"\nTOTAL INVESTMENT VALUE: {total_investment}")


with open("portfolio_report.txt", "w") as file:
    for line in report_lines:
        file.write(line + "\n")

print("\nReport saved as portfolio_report.txt")
