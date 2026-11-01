"""
Simple Python Calculator
A beginner-friendly command-line calculator.
"""

def calculate(first, operator, second):
    """Return the result of a basic arithmetic operation."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main():
    print("=== Simple Python Calculator ===")
    print("Operations: +  -  *  /")
    try:
        first = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        second = float(input("Enter the second number: "))
        result = calculate(first, operator, second)
        print(f"Result: {result:g}")
    except ValueError as error:
        print(f"Input error: {error}")
    except ZeroDivisionError as error:
        print(f"Math error: {error}")


if __name__ == "__main__":
    main()
