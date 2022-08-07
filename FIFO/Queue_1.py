class Queue:
    lst = []

    def enqueue(self, value):
        self.lst.append(value)

    def dequeue(self):
        self.lst.pop(0)

    def show(self):
        print(self.lst)

