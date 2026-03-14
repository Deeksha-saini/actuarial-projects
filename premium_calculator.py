imple Insurance Premium Calculator

sum_assured = 100000
mortality_rate = 0.002
discount_rate = 0.05

expected_claim = sum_assured * mortality_rate
net_premium = expected_claim / (1 + discount_rate)

print("Net Premium:", net_premium)
