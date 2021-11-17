expenses = []
num_expenses = int(input('Enter the number of expenses - '))

for expense in range(num_expenses):
    expenses.append(float(input(f'Enter expense {expense} ')))

total = sum(expenses)

print(f'Total expense is ${sum(expenses)}')