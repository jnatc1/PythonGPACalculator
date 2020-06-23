letter_grade_points = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0
}
total = 0             # initializes total all all grades
counter = 0         # initializes counter used to determine number of courses attempted

userGrades = input('Please enter grades in upper caps follow by a space: ') # asks for user to input grades
grades_list = userGrades.split()    # splits user input into a list
length_grades_list = len(grades_list)   # stores the lenght of the grades list to a variable

for i in range(length_grades_list):       # for loop to iterate over the grades list
    if grades_list[i] in userGrades:     # Conditional statement to check if the grade from gradeslist is in dictionary
        total = total + (letter_grade_points[grades_list[i]])     # adds key - value to total
        counter = counter + 1  # counts if the letter from grades list in the dictionary, the total of classes attempted

print(f'Total grade points earned: {total}')  # prints total points
print(f'Number of classes attempted is: {counter}') # prints total number of classes attempted
if counter > 0: # checks to make sure counter is greater than zero to avoid divide by zero exception
    gpa = total/counter  # solves for GPA
    print(f'Your GPA is: {gpa}')  # prints GPA
else:
    print(f"You're GPA is {total}")  # prints total points earned, likely will be zero if this prints

