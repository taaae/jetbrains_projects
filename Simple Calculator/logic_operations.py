def invalid_expression(expression):
    if contains_weird_characters(expression):
        return True
    if incorrect_brackets(expression):
        return True
    if incorrect_character_order(expression):
        return True
    return False


def contains_weird_characters(expression):
    return not all([ch.isalpha() or ch.isnumeric() or ch in "()+-*/^" for ch in expression])


def incorrect_brackets(expression):
    count = 0
    for ch in expression:
        if ch == ')':
            if count == 0:
                return True
            count -= 1
        if ch == '(':
            count += 1
    if count != 0:
        return True
    return False


def incorrect_character_order(expression):
    while "+-" in expression:
        expression = expression.replace("+-", "-")
    for num, ch in enumerate(expression):
        if ch == '+':
            if (num == len(expression) - 1) or (expression[num + 1] in ")-*/"):
                return True
            if (num == 0) or (expression[num - 1] in "(-*/"):
                return True
        if ch == '-':
            if (num == len(expression) - 1) or (expression[num + 1] in ")+*/"):
                return True
            if (num == 0) or (expression[num - 1] in "+*/"):
                return True
        if ch == '*' or ch == '/':
            if (num == len(expression) - 1) or (expression[num + 1] in ")+-*/"):
                return True
            if (num == 0) or (expression[num - 1] in "(+-*/"):
                return True
        if ch == '(':
            if expression[num + 1] == ')':
                return True
        if ch == ')':
            if expression[num - 1] == '(':
                return True
        if ch.isnumeric():
            if (num != len(expression) - 1) and (expression[num + 1].isalpha()):
                return True
            if (num != 0) and (expression[num - 1].isalpha()):
                return True
        if ch.isalpha():
            if (num != len(expression) - 1) and (expression[num + 1].isnumeric()):
                return True
            if (num != 0) and (expression[num - 1].isnumeric()):
                return True
        if ch == "^":
            if (num == len(expression) - 1) or (expression[num + 1] in ")-*/^"):
                return True
            if (num == 0) or (expression[num - 1] in "(-*/^"):
                return True
    return False
