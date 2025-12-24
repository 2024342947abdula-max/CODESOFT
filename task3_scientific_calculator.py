def simple_calculator():
    print("=== SIMPLE CALCULATOR ===")

    while True:
        try:
            # Prompt user for numbers
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Display operation menu
            print("\nSelect Operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Modulus (%)")
            print("6. Exit")

            choice = input("Enter your choice (1/2/3/4/5/6): ")

            # Perform calculation
            if choice == '1' or choice == '+':
                result = num1 + num2
                print(f"\nResult: {num1} + {num2} = {result}")

            elif choice == '2' or choice == '-':
                result = num1 - num2
                print(f"\nResult: {num1} - {num2} = {result}")

            elif choice == '3' or choice == '*':
                result = num1 * num2
                print(f"\nResult: {num1} * {num2} = {result}")

            elif choice == '4' or choice == '/':
                if num2 == 0:
                    print("\nERROR: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"\nResult: {num1} / {num2} = {result}")

            elif choice == '5' or choice == '%':
                if num2 == 0:
                    print("\nERROR: Division by zero is not allowed.")
                else:
                    result = num1 % num2
                    print(f"\nResult: {num1} % {num2} = {result}")

            elif choice == '6':
                print("\nExiting Calculator. Goodbye!")
                break

            else:
                print("\nInvalid operation choice. Please try again.")

        except ValueError:
            print("\nERROR: Please enter valid numeric values.")

# Run the calculator
if __name__ == "__main__":
    simple_calculator()

