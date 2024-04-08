while True:
    # Take input for the expression
    expression = input("Enter an expression (e.g., 'x + y'): ")

    # Split the expression into its components
    parts = expression.split()

    # Ensure the expression has the correct format
    if len(parts) != 3:
        print("Invalid expression. Please enter in the format 'x + y'.")
        continue

    # Extract the numbers and operator
    try:
        x = int(parts[0])
        y = int(parts[2])
    except ValueError:
        print("Invalid numbers. Please enter valid numbers.")
        continue

    operator = parts[1]

    # Perform the calculation based on the operator
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '*':
        result = x * y
    elif operator == '/':
        try:
            result = x / y
        except ZeroDivisionError:
            print("Cannot divide by zero!")
            continue
    else:
        print("Invalid operator. Please use '+', '-', '*', or '/'.")
        continue

    # Output the result
    print(f"{x} {operator} {y} = {result}")

    # Ask if user wants to continue
    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != 'yes':
        break