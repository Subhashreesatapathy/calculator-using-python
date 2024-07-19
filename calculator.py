def add(num1, num2):#add 
	return num1 + num2
def subtract(num1, num2):#sub
	return num1 - num2
def multiply(num1, num2):#mul
	return num1 * num2
def divide(num1, num2):#div
	return num1 / num2

print("Please select operation which you want to do -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")
# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if select == 1:
	print(x, "+", y, "=",
					add(x, y))

elif select == 2:
	print(x, "-", y, "=",
					subtract(x, y))

elif select == 3:
	print(x, "*", y, "=",
					multiply(x, y))

elif select == 4:
	print(x, "/", y, "=",
					divide(x, y))
else:
	print("Invalid input")

print("Calculation Done")