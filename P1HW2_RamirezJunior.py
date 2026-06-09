#Junior Ramirez
# 06/09/2026
# P1HW2
#basic math for budgeting


print("Welcome to the Budget Calculator!")
print()


# Ask user to enter their budget
budget =int(input("Enter your budget: "))

#Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas = int(input("Enter the amount you will spend on gas: "))

# Ask user for amount they will spend on accommodation
accommodation = int(input("Enter the amount you will spend on accommodation: "))

# Ask user for amount they will spend on food
food = int(input("Enter the amount you will spend on food: "))

# Add expenses
total_expenses = gas + accommodation + food

# Subtract expenses from budget

remaining_budget = budget - total_expenses

# Display results

print("------ Budget Summary------")

print("Destination: ", destination)
print("Budget: ", budget)
print()

print("Gas: ", gas)
print("Accommodation: ", accommodation)
print("Food: ", food)
print()


print("Total expenses: ", total_expenses)
print("Remaining budget: ", remaining_budget)





