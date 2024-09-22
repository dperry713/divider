def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Oops! Division by zero is not allowed."

def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Oops! That doesn't look like a valid number. Please try again.")

def main():
    print("Welcome to the Safe Division Calculator!")
    num1 = get_user_input("Enter the numerator: ")
    num2 = get_user_input("Enter the denominator: ")

    division_result = safe_divide(num1, num2)
    print(f"Result: {division_result}")

if __name__ == "__main__":
    main()
