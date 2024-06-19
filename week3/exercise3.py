class Stack():
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return len(self.stack) == 0
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            raise IndexError('Pop from empty stack')
        else:
            self.stack.pop(-1)
    def get_len(self):
        return len(self.stack)
    def peek(self, top_n = 1):
        assert top_n > 0 and isinstance(top_n,int)
        if top_n > self.get_len():
            return self.stack
        else:
            return self.stack[-top_n:]