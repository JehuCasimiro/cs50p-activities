def main():
    expression = input("Enter an arithmetic expression (x y z): ")
    x, y, z = expression.split()

    result = calculate_expression(float(x), y, float(z))
    print(f"{result:.1f}")

def calculate_expression(x, operator, z):
    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        return x / z

main()