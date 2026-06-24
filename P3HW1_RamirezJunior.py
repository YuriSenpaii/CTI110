# I was supposed to put a comment here
# Junior Ramirez
# 6/23/26
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total_sum = sum(grades)
avg = total_sum / len(grades)

# determine letter grade for average


if avg >= 90:
   letter_grade = 'A'
elif avg >= 80:
    letter_grade = 'B'
elif avg >= 70:
    letter_grade = 'C'

elif avg >= 60:
    letter_grade = 'D'


else:
    letter_grade = 'F'
 # TO DO: finish this

print()

print("-----results-----")
print(f"{'Lowest Grade: ':<21}{low}")
print(f"{'Highest Grade: ':<21}{high:.1f}")
print(f"{'Sum of Grades: ':<21}{total_sum:.1f}")
print(f"{'Average: ':<21}{avg:.2f}")
print("-----------------")
print(f" Your grade is: {letter_grade}")





