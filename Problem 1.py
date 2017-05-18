# Code tested and verified by my dude Shafim

outstanding_balance = float(input("What is the outstanding balance on your credit card?: "))
annual_interest_rate = float(input("What is the annual credit car interest rate as a decimal?: "))
min_monthly_pay_rate = float(input("What is the minimum monthly payment rate as a decimal?: "))

total = 0
for month in range(1, 13):
    print("")
    print("Month: " + str(month))
    min_monthly_pay = round((outstanding_balance * min_monthly_pay_rate), 2)
    total += min_monthly_pay
    print("Minimum monthly payment: " + str(min_monthly_pay))

    interest_paid = round(((annual_interest_rate/12) * outstanding_balance), 2)
    principal_paid = round((min_monthly_pay - interest_paid), 2)
    print("Principal paid: " + str(principal_paid))

    remaining_balance = round((outstanding_balance - principal_paid), 2)
    outstanding_balance = round((outstanding_balance - principal_paid), 2)
    print("Remaining balance: " + str(remaining_balance))
print("")
print("RESULT:")
print("Total paid: " + str(total))
print("Remaining balance: " + str(outstanding_balance))
