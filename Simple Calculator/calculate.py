from final_calculation import final_calculation
from logic_operations import invalid_expression

variables = {}


def main(calc_input) -> "True to brake":
    if calc_input.startswith('/'):
        if calc_input == '/exit':
            print("Bye!")
            return True
        if calc_input == '/help':
            print("The program calculates the sum of numbers")
        else:
            print("Unknown command")
        return
    if calc_input == '':
        return
    if '=' in calc_input:
        identifier = calc_input.split('=')[0].strip()
        if not identifier.isalpha():
            print("Invalid identifier")
            return
        if len(calc_input.split('=')) != 2:
            print("Invalid assignment")
            return
        result = calculate(calc_input.split('=')[1])
        if result == "Invalid expression":
            print("Invalid assignment")
            return
        if result == "Unknown variable":
            print("Unknown variable")
            return
        variables[identifier] = result
        return
    print(calculate(calc_input))


def calculate(expression):
    expression = expression.replace(' ', '')
    if invalid_expression(expression):
        return "Invalid expression"
    sorted_variables = sorted(variables, key=len)[::-1]
    for var in sorted_variables:
        expression = expression.replace(var, str(variables[var]))
    while "+-" in expression:
        expression = expression.replace("+-", "-")
    if any([ch.isalpha() for ch in expression]):
        return "Unknown variable"
    while "+++" in expression or "---" in expression:
        expression = expression.replace("+++", "+")
        expression = expression.replace("---", "-")
    expression = expression.replace("++", "+")
    expression = expression.replace("--", "+")
    return int(final_calculation(expression))
