# Loan Amortization Model

loan_amount = 200000
annual_interest_rate = 0.06
years = 5

monthly_rate = annual_interest_rate / 12
months = years * 12

monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)

balance = loan_amount

print("Month   Payment   Remaining Balance")

for month in range(1, months + 1):
    interest = balance * monthly_rate
    principal = monthly_payment - interest
    balance = balance - principal
    
    print(month, round(monthly_payment,2), round(balance,2))
