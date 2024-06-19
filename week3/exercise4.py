class Queue():
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return len(self.queue) == 0
    def enqueue(self, element):
        self.queue.append(element)
    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Pop from empty queue')
        else:
            self.queue.pop(0)
    def get_len(self):
        return len(self.queue)
    def front(self, top_n = 1):
        assert top_n > 0 and isinstance(top_n,int)
        if top_n > self.get_len():
            return self.queue
        else:
            return self.queue[:top_n]