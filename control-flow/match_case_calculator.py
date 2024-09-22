X = int(input("Enter the first number:"))
Y = int(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

if operation == "+":
    print("The result is " + str(X + Y) + ".")
elif operation == "-":
    print("The result is " + str(X - Y) + ".")
elif operation == "*":
    print("The result is " + str(X * Y) + ".")
elif operation == "/":
    if Y == 0:
        print("Cannot divide by zero.")
    else:
        print("The result is " + str(int(X / Y)) + ".")
    