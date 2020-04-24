from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.list_buffer_contents = []

    def append(self, item):
        if len(self.list_buffer_contents) == self.capacity:
            oldest_item = self.storage.tail.value
            ind = self.list_buffer_contents.index(oldest_item)
            self.list_buffer_contents.remove(oldest_item)
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)
            self.list_buffer_contents.insert(ind, item)
        else:
            self.storage.add_to_head(item)
            self.list_buffer_contents.append(item)

    def get(self):
        # Note:  This is the only [] allowed
        # list_buffer_contents = []

        # TODO: Your code here

        return self.list_buffer_contents


buffer = RingBuffer(3)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')

print(buffer.get())

buffer.append('e')

print(buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
