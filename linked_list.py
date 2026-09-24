# linked_list.py
# A singlely linked list with a tracked head
# Modified by: Tristan Crawford Jr

from collections.abc import MutableSequence

class LLNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(MutableSequence):
    def __init__(self, iterable=None):
        self.head = None
        self._length = 0
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if index < 0:
            index += self._length
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def __setitem__(self, index, value):
        if index < 0:
            index += self._length
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def __delitem__(self, index):
        if index < 0:
            index += self._length

        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head

            for _ in range(index - 1):
                current.next = current.next

            current.next = current.next.next

        self._length -= 1

    def insert(self, index, value):
        if index < 0:
            index += self._length

        if index < 0:
            index = 0

        if index > self._length:
            index = self._length

        new_node = LLNode(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head

            for _ in range(index - 1):
                current.next = current.next

            new_node.next = current.next
            current.next = new_node

        self._length += 1

    def append(self, value):
        self.insert(self._length, value)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self):
        return "LinkedList([" + ", ".join(repr(x) for x in self) + "])"
