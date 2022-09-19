from collections import deque


def final_calculation(expression: str) -> int:
    expression = to_postfix(expression)
    my_stack = deque()
    for element in expression:
        if is_num(element):
            my_stack.append(int(element))
            continue
        number2, number1 = my_stack.pop(), my_stack.pop()
        my_stack.append(do_operation(number1, number2, element))
    return my_stack.pop()


def to_postfix(expression: str) -> deque:
    operation_precedence = {"*": 1, "/": 1, "+": 0, "-": 0, "^": 2}
    expression = parsed_expression(expression)
    result = deque()
    operand_stack = deque()
    for element in expression:
        if is_num(element):
            result.append(element)
            continue
        if not operand_stack or (operand_stack[len(operand_stack) - 1] == "(" and element in "+-*/^"):
            operand_stack.append(element)
            continue
        if element == "(":
            operand_stack.append(element)
            continue
        if element == ")":
            while operand_stack[len(operand_stack) - 1] != "(":
                result.append(operand_stack.pop())
            operand_stack.pop()
            continue
        if operation_precedence[element] > operation_precedence[operand_stack[len(operand_stack) - 1]]:
            operand_stack.append(element)
            continue
        while operand_stack and operand_stack[len(operand_stack) - 1] != "(" \
                and operation_precedence[element] <= operation_precedence[operand_stack[len(operand_stack) - 1]]:
            result.append(operand_stack.pop())
        operand_stack.append(element)
    while operand_stack:
        result.append(operand_stack.pop())
    return result


def parsed_expression(expression: str):
    ans = []
    current = ""
    for num, char in enumerate(expression):
        if char.isnumeric():
            current += char
        elif char == "-" and (num == 0 or expression[num - 1] == "("):
            current += char
        else:
            if current != "":
                ans.append(current)
                current = ""
            ans.append(char)
    if current != "":
        ans.append(current)
    return ans


def do_operation(num1, num2, operation: chr):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "^":
            return num1 ** num2


def is_num(string):
    return string.isnumeric() or (string[0] == "-" and string != "-")
