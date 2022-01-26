
from postfix_v2 import convert_infix
from linkstack import Stack

OPERATORS = {"+": lambda x,y: x+y,
             "-": lambda x,y: x-y,
             "*": lambda x,y: x*y,
             "/": lambda x,y: x/y}

class ExpressionTree:

    def __init__(self,root):
        self.root = root

    def __len__(self):
        if self.root:
            return len(self.root)
        else:
            return 0

    def display(self):
        if self.root:
            self.root.display_subtree("X")

    def prefix_expr(self):
        if self.root is not None:
            return self.root.prefix_expr()
        return ""

    def postfix_expr(self):
        if self.root is not None:
            return self.root.postfix_expr()
        return ""

    def infix_expr(self):
        if self.root is not None:
            return self.root.infix_expr()
        return ""

    def calculate(self):
        if self.root is None:
            raise Exception("Alex lazy")
        return self.root.calculate()
    

class TreeNode:

    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def __len__(self):
        my_len = 1
        if self.left:
            my_len += len(self.left)
        if self.right:
            my_len += len(self.right)
        return my_len

    def display_subtree(self,loc_name):
        print(f"{loc_name}: {self.value}")
        if self.left:
            self.left.display_subtree(loc_name+"L")
        if self.right:
            self.right.display_subtree(loc_name+"R")

    def prefix_expr(self):
        the_expr = ""
        the_expr += str(self.value)
        if self.left is not None:
            the_expr += " "
            the_expr += self.left.prefix_expr()
        if self.right is not None:
            the_expr += " "
            the_expr += self.right.prefix_expr()
        return the_expr

    def postfix_expr(self):
        the_expr = ""
        if self.left is not None:
            the_expr += self.left.postfix_expr()
            the_expr += " "
        if self.right is not None:
            the_expr += self.right.postfix_expr()
            the_expr += " "
        the_expr += str(self.value)
        return the_expr

    def infix_expr(self):
        the_expr = ""
        if self.value in OPERATORS:
            the_expr += "("
        if self.left is not None:
            the_expr += self.left.infix_expr()
            the_expr += " "
        the_expr += str(self.value)
        if self.right is not None:
            the_expr += " "
            the_expr += self.right.infix_expr()
        if self.value in OPERATORS:
            the_expr += ")"
        return the_expr

    def calculate(self):
        if self.value in OPERATORS:
            return OPERATORS[self.value](self.left.calculate(),self.right.calculate())
        else:
            return self.value

if __name__ == "__main__":
    infix_expr = ["(","4","+","5",")","*","8","-","2"]
    postfix_expr = convert_infix(*infix_expr)
    node_stack = Stack()
    for token in postfix_expr:
        
        if token in OPERATORS:
            new_node = TreeNode(token)
            new_node.right = node_stack.pop()
            new_node.left = node_stack.pop()
        else:
            new_node = TreeNode(int(token))
        node_stack.push(new_node)
    expr_tree = ExpressionTree(node_stack.pop())
    expr_tree.display()
    print(f"Pre: {expr_tree.prefix_expr()}")
    print(f"Post: {expr_tree.postfix_expr()}")
    print(f"In: {expr_tree.infix_expr()}")
    print(f"Result: {expr_tree.calculate()}")
