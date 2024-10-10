# Write a Python program to input a positive integer. Display correct message for correct and incorrect input. (Use Exception Handling

num = int (input("Enter Any Positive number:"))
try:
 if num >= 0:
    raise ValueError("Positive Number-Input Number is Correct")
 else:
    raise ValueError("Negative Number-Input Number is InCorrect")
except ValueError as e:
    print(e)