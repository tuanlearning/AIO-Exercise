class Queue():
    def __init__(self, capacity):
        assert isinstance(capacity, int), "Capacity has to be an integer"
        self.queue = []
        self.capacity = capacity
    def is_empty(self):
        return len(self.queue) == 0
    def is_full(self):
        return len(self.queue) == self.capacity
    def enqueue(self, element):
        if self.is_full():
            print("Queue has already reached full capacity")
        else:
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