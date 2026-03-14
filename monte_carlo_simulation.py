# Monte Carlo Investment Simulation

import numpy as np

initial_investment = 10000
years = 10
simulations = 1000
mean_return = 0.07
volatility = 0.15

results = []

for i in range(simulations):
    value = initial_investment
    
    for year in range(years):
        random_return = np.random.normal(mean_return, volatility)
        value = value * (1 + random_return)
    
    results.append(value)

average_value = np.mean(results)

print("Initial Investment:", initial_investment)
print("Average Value After", years, "Years:", round(average_value,2))
