while True:
    
        b = int(input("Enter the first number: "))
        c = int(input("Enter the second number: "))
        a = input("Enter the operation to be performed (+, -, /, *, %): ")
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
            
        X = input("Enter 'Yes' if you want to do more calculations and 'No' to exit: ")
        if X.lower() == "yes":
            continue
        else:
            break


        
