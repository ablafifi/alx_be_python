X = int(input("Enter the first number:"))
Y = int(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")
match operation:
    case"+":
        print("The result is " + str(X + Y) + ".")
    case "-":
        print("The result is " + str(X - Y) + ".")
    case "*":
        print("The result is " + str(X * Y) + ".")
    case "/":
        if Y == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is " + str(int(X / Y)) + ".")
    