def are_brackets_balanced(expression):
    stack = []
    
    for char in expression:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        
        elif char == ')' or char == '}' or char == ']':
            if len(stack) == 0:
                return False

            last_open_bracket = stack.pop()

            if last_open_bracket == '(' and char != ')':
                return False
            if last_open_bracket == '{' and char != '}':
                return False
            if last_open_bracket == '[' and char != ']':
                return False

    if len(stack) == 0:
        return True
    else:
        return False

balanced_expression = "{ ( [ ] ) }"
unbalanced_expression = "{ ( [ ) ] }"

print(balanced_expression + " is balanced: " + str(are_brackets_balanced(balanced_expression)))
print(unbalanced_expression + " is balanced: " + str(are_brackets_balanced(unbalanced_expression)))