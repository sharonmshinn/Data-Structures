class LinkStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        self.size += 1
        new_node = LinkStackNode(value)
        new_node.below = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise EmptyError("Stack is empty!")
        self.size -= 1
        output = self.top.value
        self.top = self.top.below
        return output

    def peek(self):
        if self.top is None:
            raise EmptyError("Stack is empty!")
        return self.top.value

    def __len__(self):
        return self.size

    def other_len(self):
        node_count = 0
        next_node = self.top
        while next_node is not None:
            node_count +=1
            next_node = next_node.below
        return node_count

    def is_empty(self):
        return self.top is None

    def __str__(self):
        output = "Stack:["
        next_node = self.top
        if next_node is not None:
            output += f"{next_node.value!r}"
            next_node = next_node.below
            while next_node is not None:
                output += ","
                output += f"{next_node.value!r}"
                next_node = next_node.below
        output += "]"
        return output

class LinkStackNode:
    def __init__(self, value):
        self.value = value
        self.below = None

class EmptyError(Exception):
    '''Raised if stack is empty and top node is None'''
    pass
