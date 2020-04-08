class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    # Additional methods we can include:
    def is_empty(self):
        return self.items == []

    # Get top element of stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return 'Stack is empty'

    def get_stack(self):
        return self.items


s = Stack()
print(s.is_empty())  # True
s.push("A")
s.push("B")
print(s.get_stack())  # ['A', 'B']
s.push("C")
print(s.get_stack())  # ['A', 'B', 'C']
s.pop()
print(s.get_stack())  # ['A', 'B']
print(s.is_empty())  # False
