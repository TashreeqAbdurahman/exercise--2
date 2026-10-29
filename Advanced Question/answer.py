-0,0 +1,70 
import math
a = 5
b = 10
c = 7

a += 3
b *= 2
c %= 4

final_result = math.sqrt (a**2 + b**2 + c**2)
print(round(final_result, 2))

x = int(input("Enter your number"))
y = int(input("Enter your number"))
z = int(input("Enter your number"))

is_even = x % 2 == 0
is_positive = y > 0
is_in_range = z >= 10 and z <= 50
final_condition = is_even and is_positive and is_in_range
print(final_condition)

score = float(input("Enter your score"))

bonus = 5
penalty = 10

final_score = score + 5 - 10
final_score = max(0, min(100, final_score))

if final_score >= 90:
 result = "A"
if final_score >= 80:
  result = "B"
if final_score >= 70:
  result = "C"
if final_score >= 60:
 result = "D"
else :
 result = "F"

print(final_score)
print(result)

num1 = int(input("Enter your number"))
num2 = int(input("Enter your number"))

operation = input("Enter your operation: operation (+, -, *, /, %, **)")
if operation == "+":
 answer = num1 + num2
if operation == "-":
 answer = num1 - num2
if operation == "*":
 answer = num1 * num2
if operation == "**":
 answer = num1 ** num2

if operation == "%":
 if num2 != 0:
     answer = num1 % num2
else:
 answer = "cannot divide by zero"

if operation == "/":
    if num2 != 0:
     answer = num1 / num2
    else:
     answer = "cannot divide by zero"

print (answer)