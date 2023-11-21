class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)

# Example usage:
custom_queue = Queue()
custom_queue.enqueue(10)
custom_queue.enqueue(20)
custom_queue.enqueue(30)

print("Queue size:", custom_queue.size())  # Output: 3
print("Front of the queue:", custom_queue.peek())  # Output: 10

while not custom_queue.is_empty():
    print("Dequeued:", custom_queue.dequeue())

