# Financial Modeling: Investment Growth Model

initial_investment = 10000
interest_rate = 0.07
years = 10

value = initial_investment

print("Year   Investment Value")

for year in range(1, years + 1):
    value = value * (1 + interest_rate)
    print(year, "   ", round(value, 2))
