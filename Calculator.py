class Calculator:

    def API(self, math_expression):
        if self.check_parentheses(math_expression):
            return "Invalid Expression"
        elif self.illegal_negative(math_expression):
            return "Invalid Negative"
        elif self.detect_characters(math_expression):
            return "Illegal Character(s)"
        elif self.illegal_parenthesis(math_expression):
            return "Invalid Expression"
        elif self.detect_multiple_operators(math_expression):
            return "Operator needs two operands"
        elif self.prevent_decimal(math_expression):
            return "Cannot compute decimals...yet"
        else:
            math_expression = self.infix_to_postfix(math_expression)
            if math_expression == "Error":
                return "Invalid Expression"
            return self.evaluate_postfix(math_expression)

    def prevent_decimal(self, expression):
        token_list = list(expression)
        for token in token_list:
            if token == ".":
                return True
        return False

    def illegal_parenthesis(self, expression):
        token_list = list(expression)
        index_counter = 0
        for token in token_list:
            index_counter += 1
            if token == "(":
                if token_list.index(token) == 0:
                    return False
                elif token_list[token_list.index(token)-1] in "0123456789":
                    return True
                else:
                    return False
            if token == ")":
                if index_counter == len(token_list) and len(token_list) != 1:
                    return False
                elif token_list.index(token) == 0:
                    return True
                elif token_list[token_list.index(token) + 1] in "0123456789":
                    return True
                else:
                    return False
        return False

    def illegal_negative(self, expression):
        token_list = list(expression)
        index_counter = 0
        for token in token_list:
            index_counter += 1
            if token == "n":
                if index_counter == len(token_list):
                    return True
                elif token_list.index(token) == 0:
                    return False
                elif token_list[token_list.index(token)+1] in "0123456789":
                    if token_list[token_list.index(token) - 1] in "0123456789)":
                        return True
                    return False
                else:
                    return True
        return False

    def detect_characters(self, expression):
        token_list = list(expression)
        for token in token_list:
            if token in "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`~,<.>?;:'[{|]}!@#$%&=":
                return True
            else:
                return False

    def detect_multiple_operators(self, expression):
        token_list = list(expression)
        op_count = 0
        for token in token_list:
            if token in "/+-*":
                op_count += 1
            else:
                op_count = 0
            if op_count == 2:
                return True
        return False

    def check_parentheses(self, expression):
        token_list = list(expression)
        left_par_count = 0
        right_par_count = 0
        dummy = 0
        for token in token_list:
            if token == "(":
                left_par_count += 1
            elif token == ")":
                right_par_count += 1
            else:
                dummy += 0
        if left_par_count != right_par_count:
            return True
        else:
            return False

    def infix_to_postfix(self, infix):
        precedence = {
            "^": 4,
            "*": 3,
            "/": 3,
            "+": 2,
            "-": 2,
            "(": 1
        }
        op_stack = []
        postfix = []
        digit_list = []
        token_list = list(infix)
        index_counter = 0

        for token in token_list:
            index_counter += 1
            if token in "0123456789n":
                if index_counter == len(token_list):
                    digit_list.append(token)
                    multi_digit_num = "".join(digit_list)
                    postfix.append(multi_digit_num)
                elif token_list[token_list.index(token)+1] in "1234567890":
                    if token == "n":
                        digit_list.append("-")
                    else:
                        digit_list.append(token)
                else:
                    digit_list.append(token)
                    multi_digit_num = "".join(digit_list)
                    postfix.append(multi_digit_num)
                    while len(digit_list) != 0:
                        digit_list.pop()
            elif token == "(":
                op_stack.append(token)
            elif token == ")":
                try:
                    top_of_stack = op_stack.pop()
                    while top_of_stack != "(":
                        postfix.append(top_of_stack)
                        top_of_stack = op_stack.pop()
                except IndexError as exception:
                    print(exception)
                    return "Error"
            else:
                while len(op_stack) != 0 and precedence[self.peek(op_stack.copy())] >= precedence[token]:
                    postfix.append(op_stack.pop())
                op_stack.append(token)

        while len(op_stack) != 0:
            postfix.append(op_stack.pop())

        return " ".join(postfix)

    def evaluate_postfix(self, postfix):
        operand_list = []
        token_list = postfix.split()

        for token in token_list:
            if token not in "+-()*^/":
                operand_list.append(int(token))
            else:
                operand_one = operand_list.pop()
                operand_two = operand_list.pop()
                result = self.perform_calc(operand_one, operand_two, token)
                operand_list.append(result)
        return str(operand_list.pop())

    def perform_calc(self, op1, op2, token):
        if token == "*":
            return op1*op2
        elif token == "/":
            return op1/op2
        elif token == "+":
            return op1+op2
        elif token == "^":
            return op2**op1
        else:
            return op2-op1

    def peek(self, list_copy):
        return list_copy.pop()
