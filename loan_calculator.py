# Get the loan details
money_owed = float(input('How much money in dollars?\n')) # 50,000
apr = float(input('What is annual percentage rate?\n')) # 3%
payment = float(input('Monthly payment?\n')) # 1000
months = int(input('Tenure?\n')) # 24

# Divide apr by 100 then by 12 to calulate monthly rate
monthly_rate = apr/100/12

for month in range(months):
    # Add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print('The last payment is', money_owed)
        print('You paid of the loan in', month+1, 'months')
        break
    # Make payment
    money_owed = money_owed - payment

    # Print results
    print("Paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("Now I owe", money_owed)
