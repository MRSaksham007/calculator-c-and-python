def calculator(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0:
            return "Error: Division by zero is not allowed"
        return x / y
    else:
        return "Invalid operator"


a = int(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = int(input("Enter second number: "))

result = calculator(a, b, op)
print("Result:", result)
