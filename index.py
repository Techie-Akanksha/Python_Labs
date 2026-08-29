#1. Write a program that asks the user for a number and prints whether it is even or odd. 
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


#2. Simple Calculator
first_number = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))
result = 0
def calculate(first_number, operator, second_number):
    if operator == '+':
        result = first_number + second_number
        return result
    elif operator == '-':
        result = first_number - second_number
        return result
    elif operator == '*':
        result = first_number * second_number
        return result   
    elif operator == '/':
        if second_number != 0:
            result = first_number // second_number
            return result   
        else:
            return "Error: Division by zero."
    else:
        return "Error: Invalid operator."

result = calculate(first_number, operator, second_number)
print(f"The result is: {result}")

#3. FizzBuzz : Print numbers from 1 to 100.
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)