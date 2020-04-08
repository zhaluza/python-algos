# Use a stack to check whether a string has balanced usage of parentheses and brackets
# Balanced: {([()])}
# Not Balanced: {([())}]

# Could alternatively import the stack created in stack_example.py
# from stack_example import Stack


class Stack():
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    # peek at top of stack
    def peek(self):
        return self.items[-1]


def isMatch(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    # initialize a stack
    # loop through the string
    # if the current element is an opening paren — ([{ — push to the stack
    # if the current element is a closing paren — )]} — and the last stack element is a matching open parens, pop the open parens off the stack and keep moving
    # else, return false
    # return true at the end

    stack = Stack()
    for el in paren_string:
        if el in '([{':
            stack.push(el)
        elif isMatch(stack.peek(), el):
            stack.pop()
        else:
            return False
    return True


print(is_paren_balanced('{([())}]'))  # False
print(is_paren_balanced('{([()])}'))  # True
