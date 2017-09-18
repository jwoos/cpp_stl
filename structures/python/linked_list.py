"""
Singly linked list
"""


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 1 if head else 0

    def append(self, data):
        node = LinkedListNode(data=data)

        if not self.size:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next

        self.size += 1

    def pop(self, node=False):
        previous = self.get(self.size - 1)

        previous.next = current.next
        self.size -= 1
        return current if node else current.data

    def get(self, index, node=False):
        current = self.head

        while index > 0 and current.next is not None:
            index -= 1
            current = current.next

        if index != 0:
            raise Exception('Not Found')

        return current if node else current.data

    def insert(self, index, data):
        # head
        if index == 0:
            next = self.head
            self.head = LinkedListNode(data=data)
            self.head.next = next
        #tail
        elif index == self.size - 1:
            self.append(data)
        # other
        else:
            previous = self.get(index - 1, node=True)
            current = LinkedListNode(data=data)
            current.next = previous.next
            previous.next = current

        self.size += 1

    def delete(self, index):
        # head
        if index == 0:
            current = self.head
            self.head = self.head.next
            # remove from scope
            del current
        #tail
        elif index == self.size - 1:
            self.pop(index)
        # other
        else:
            previous = self.get(index, node=True)
            current = previous.next
            previous.next = current.next
            # remove from scope
            del current

        self.size -= 1

    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print()


class LinkedListNode:
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data
