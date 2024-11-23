import calculus_tools

def solve_expression():
    try:
        print("Welcome to the Advanced Calculus Tool!")
        print("Supported Features:")
        print("1. Derivatives (Standard or Leibniz's theorem).")
        print("2. Maclaurin Series.")
        print("3. Taylor Series.")

        # Choose operation
        choice = input("\nChoose an option (1: Derivative, 2: Maclaurin Series, 3: Taylor Series): ")

        if choice == "1":
            # Derivative (Standard or Leibniz's theorem)
            expr = input("Enter the mathematical expression: ").lower()
            var = input("Enter the variable with respect to which you want to differentiate (e.g., x): ").lower()
            order = int(input("Enter the order of the derivative (e.g., 1 for first derivative): "))
            
            # Call the function from the library
            result = calculus_tools.calculate_derivative(expr, var, order)
            print(f"\nThe {order}-order derivative of {expr} with respect to {var} is: {result}")

        elif choice == "2":
            # Maclaurin Series
            expr = input("Enter the mathematical expression: ").lower()
            var = input("Enter the variable (e.g., x): ").lower()
            terms = int(input("Enter the number of terms for the series: "))
            
            # Call the function from the library
            result = calculus_tools.maclaurin_series(expr, var, terms)
            print(f"\nThe Maclaurin series of {expr} up to {terms} terms is: {result}")

        elif choice == "3":
            # Taylor Series
            expr = input("Enter the mathematical expression: ").lower()
            var = input("Enter the variable (e.g., x): ").lower()
            point = float(input("Enter the point around which to expand (e.g., 0 for Maclaurin): "))
            terms = int(input("Enter the number of terms for the series: "))
            
            # Call the function from the library
            result = calculus_tools.taylor_series(expr, var, point, terms)
            print(f"\nThe Taylor series of {expr} around {point} up to {terms} terms is: {result}")

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    except Exception as e:
        print(f"Error: {e}")
        print("Invalid input. Ensure your expression and variable are correctly formatted.")

if __name__ == "__main__":
    solve_expression()
