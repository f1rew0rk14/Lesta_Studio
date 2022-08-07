class Queue:
    head = None

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def enqueue(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

    def show(self):
        node = self.head
        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    def dequeue(self):
        self.head = self.head.next_node


