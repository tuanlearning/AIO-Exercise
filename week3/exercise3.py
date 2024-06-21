class Stack():
    def __init__(self, capacity):
        assert isinstance(capacity, int), "Capacity has to be an integer"
        self.stack = []
        self.capacity = capacity
    def is_empty(self):
        return len(self.stack) == 0
    def is_full(self):
        return len(self.stack) == self.capacity
    def push(self, element):
        if self.is_full():
            print("Stack already reached full capacity")
        else:
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