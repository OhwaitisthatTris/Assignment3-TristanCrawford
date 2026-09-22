# dynamic_array.py
# A dynamic array using Python's array module
# Modified by: Tristan Crawford

from array import array
from collections.abc import MutableSequence

class DynamicArray(MutableSequence):
    
    GROWTH_FACTOR = 2
    INITIAL_CAPACITY = 10

    def __init__(self, iterable=None):
        self._capacity = DynamicArray.INITIAL_CAPACITY
        self._length = 0
        self._array = array('i', [0] * self._capacity)
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
        return self._array[index]
    
    def __setitem__(self, index, value):
        if index < 0:
            index += self._length
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")
        self._array[index] = value

    def __delitem__(self, index):
      if index < 0:
        index += self._length

if index < 0 or index >=    
self._length:   
        raise IndexError("Index out of range")
 for i in range(index, self._length - 1):
        self._array[i] = self._array[i + 1]
self._length -= 1
        pass

 def insert(self, index, value):
    if self._length == self._capacity:
        self._resize()

    if index < 0:
        index += self._length

    if index < 0:
        index = 0

    if index > self._length:
        index = self._length

    for i in range(self._length, index, -1):
        self._array[i] = self._array[i - 1]

    self._array[index] = value
    self._length += 1
        pass

def _resize(self):
    new_capacity = self._capacity * DynamicArray.GROWTH_FACTOR

    new_array = array('i', [0] * new_capacity)

    for i in range(self._length):
        new_array[i] = self._array[i]

    self._array = new_array
    self._capacity = new_capacity
        pass

    def __repr__(self):
        return "DynamicArray([" + ", ".join(repr(self._array[i]) for i in range(self._length)) + "])"
    
    def __iter__(self):
        for i in range(self._length):
            yield self._array[i]
    
    def append(self, value):
        self.insert(self._length, value)
