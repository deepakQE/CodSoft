while True:
    X = input("Enter 'Yes' if you want to do more calculations and 'No' to exit: ")
    if X == "Yes" or "yes":
        a = input("Enter the operation to be performed (+, -, /, *, %): ")
        b = int(input("Enter the first number: "))
        c = int(input("Enter the second number: "))
        if a == '+':
            d = b + c
        elif a == '-':
            d = b - c
        elif a == '/':
            d = b / c
        elif a == '*':
            d = b * c
        elif a == '%':
            d = b % c
        else:
            print("Invalid operation. Please retry.")
            continue
        print("Your result is:", d)
    else:
        break
    
