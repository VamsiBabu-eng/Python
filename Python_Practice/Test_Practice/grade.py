# Take input from user
grade = int(input("Enter your grade (0-100): "))

# Check conditions
if 90 <= grade <= 100:
    print("Distinction")
elif 75 <= grade <= 89:
    print("Credit")
elif 50 <= grade <= 74:
    print("Pass")
elif 0 <= grade < 50:
    print("Fail")
else:
    print("Invalid input! Please enter a value between 0 and 100.")