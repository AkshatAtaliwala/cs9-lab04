class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self.items = []

    def isEmpty(self):
        """Check if the stack is empty"""
        return not bool(self.items)

    def push(self, item):
        """Add an item to the stack"""
        self.items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self.items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self.items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self.items)
