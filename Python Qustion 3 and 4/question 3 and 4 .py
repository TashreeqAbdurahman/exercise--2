x = 5
y = 4

x += 3 
y *= 2 

result = x / y

print(result)

a = 10
b = 4
c = 5

cond1 = a > b
cond2 = b % 2 == 0
cond3 = c > 0

final_condition = cond1 or (cond2 and cond3)

print(final_condition)

score = float(input("Enter a test score (0-100):"))

if score >= 90 and score <=100:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"    
elif score >= 60:
    grade = "D"  
else:
    grade = "F"  

    print(f"The grade for a score of {score} is : {grade}\n")   

print(f"The grade for a score of {score} is : {grade}\n")



try:
    num1 = float(input("Enter the first number (num1): "))
    operation = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    result = None 
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
        
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
        
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
        
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
            
    else:
        print("Invalid operation selected.")

except ValueError:
    print("Error: Please enter valid numbers only.")

