# Junior Ramirez
# 6/27/2026
#P3HW2_Salary
# This program calculates the salary of an employee based on their hourly wage and hours worked.


# get inputs from user

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))

# calculate hours and pay using if/else statements

if hours > 40:
    reg_hours = 40.0
    overtime_hours = hours - 40.0

else:
    reg_hours = hours
    overtime_hours = 0.0

reg_pay = reg_hours * pay_rate
overtime_pay = overtime_hours * (pay_rate * 1.5)
gross_pay = reg_pay + overtime_pay

# display results

print("-------------------------------")
print("Employee Name:", name)
print()

# print the headers

print("----------------------------------------")
print("Employee name:", name)
print("Pay rate:", pay_rate)
print("Hours worked:", hours)
print("Overtime hours:", overtime_hours)
print("Overtime pay:", overtime_pay)
print("Regular hours pay:", reg_pay)
print("Gross pay:", gross_pay)

