
class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def first(self):
        if self.size == 0:
            raise EmptyError()
        return self.front.value
    def enqueue(self,value):
        new_node = QueueNode(value)
        if self.size == 0:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node
        self.size += 1
    def dequeue(self):
        if self.size == 0:
            raise EmptyError()
        return_value = self.front.value
        #self.size -= 1
        if self.size == 1:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
        self.size -= 1
        return return_value
    def __str__(self):
        repr_values = []
        next_node = self.front
        while next_node is not None:
            repr_values.append(repr(next_node))
            next_node = next_node.next
        return f"[{','.join(repr_values)}]"

class EmptyError(Exception):
    pass

class QueueNode:
    def __init__(self,value):
        self.value = value
        self.next = None
