
class AVLTree:
    
    def __init__(self):
        self.root = None
    
    def lookup(self,value):
        if self.root == None:
            return False
        else:
            self.root.lookup(value)
    
    def add(self,value):
        if self.root == None:
            self.root = AVLTreeNode(None, value)
        else:
            self.root = self.root.add(value)
    
    def remove(self,value):
        if self.root is not None:
            self.root = self.root.remove(value)
        else:
            return False

    
    def __len__(self):
        if self.root is None:
            return 0
        else:
            return self.root.size()
            
    def display(self):
        if self.root is None:
            print("[Empty tree]")
        else:
            self.root.display()
    
    def assert_valid(self):
        if self.root is not None:
            self.root.assert_avl()
            self.root.assert_tree()
            self.root.assert_sorted()

class AVLTreeNode:
    
    def __init__(self,parent,value):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
    
    def lookup(self,value):
        if self.value == value:
            return True
        elif value > self.value and self.right is not None:
            self.right.lookup(value)
        elif value < self.value and self.left is not None:
            self.left.lookup(value)
        elif self.left is None and self.right is None:
            return False
    
    def root(self):
        if self.parent is None:
            return self
        elif self.parent is not None:
            return self.parent.root()

    
    def add(self,value):
        if value > self.value and self.right is not None:
            self.right.add(value)
        elif value < self.value and self.left is not None:
            self.left.add(value)
        elif value > self.value and self.right is None:
            self.right = AVLTreeNode(self, value)
            self.right.check_up()
        elif value < self.value and self.left is None:
            self.left = AVLTreeNode(self, value)
            self.left.check_up()
        elif value == self.value:
            return 
        
        return self.root()
    
    
    def rightmost_descendent(self):
        if self.right is None:
            return self 
        else:
            return self.right.rightmost_descendent()
        
    
    def notify_parent(self,new):
        if self is self.parent.left:
            self.parent.left = new
        elif self is self.parent.right:
            self.parent.right = new
            
    
    def remove(self,value):
        if self.value < value and self.right is not None:
            return self.right.remove(value)
        elif self.value > value and self.left is not None:
            return self.left.remove(value)
        elif self.value < value and self.right is None:
            return self.root
        elif self.value > value and self.left is None:
            return self.root
        elif self.value == value:
        #deleting root cases
            return_root = self.parent
            #no children
            if self.left is None and self.right is None:
                if self.parent is None:
                    return None
                else:
                    self.notify_parent(None)
                    self.check_up()
                return return_root.root()
            #right child
            elif self.left is None and self.right is not None:)
                temp = self.right
                self.value = temp.value
                self.check_up()
                return self.right.remove(temp.value)
            #left child
            elif self.left is not None and self.right is None:
                temp = self.left
                self.value = temp.value
                self.check_up()
                return self.left.remove(temp.value)
            #two children
            elif self.left is not None and self.right is not None:
                new_root = self.left.rightmost_descendent()
                self.value = new_root.value
                self.check_up()
                return self.left.remove(new_root.value)
            return self.root()
                    

            
    
    def height(self):
        if self.left and self.right is not None:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left is not None:
            return 1 + self.left.height()
        elif self.right is not None:
            return 1 + self.right.height()
        else:
            return 1
    
    def balance_factor(self):
        if self.right is None and self.left is None:
            return 0
        elif self.right is None and self.left is not None:
            return 0 - self.left.height()
        elif self.right is not None and self.left is None:
            return self.right.height() - 0
        else:
            return self.right.height() - self.left.height()

        
    
    def rotate_right(self):
        temp = None
        if self.left.right is not None:
            temp = self.left.right
        if self.parent is not None:
            self.notify_parent(self.left)
        self.left.parent = self.parent
        self.left.right = self
        self.parent = self.left
        self.left = None
        if temp is not None:
            temp.parent = self
            self.left = temp
            
        
    
    def rotate_left(self):
        temp = None
        if self.right.left is not None:
            temp = self.right.left
        if self.parent is not None:
            self.notify_parent(self.right)
        self.right.parent = self.parent
        self.right.left = self
        self.parent = self.right
        self.right = None
        if temp is not None:
            temp.parent = self
            self.right = temp

        
    
    def check_up(self):
        bf = self.balance_factor()
        if bf == -2:

            #left-right
            if self.left.balance_factor() == 1:
                self.left.rotate_left()
                self.rotate_right()

            #left-left
            elif self.left.balance_factor() <= 0:
                self.rotate_right()

        elif bf == 2:
            if self.right.balance_factor() >= 0:)
                self.rotate_left()
            
            #right-left
            elif self.right.balance_factor() == -1:
                self.right.rotate_right()
                self.rotate_left()
        if self.parent is not None:
            return self.parent.check_up()
        return self.root()
            
    
    def display(self,prefix="X"):
        print(f"{prefix}: [{self.value}]")
        if self.left is None:
            print(f"{prefix}L: -")
        else:
            self.left.display(prefix+"L")
        if self.right is None:
            print(f"{prefix}R: -")
        else:
            self.right.display(prefix+"R")
    
    def __repr__(self):
        return f"[AVLTreeNode:{self.value}]"
    
    def assert_sorted(self):
        if self.left is not None:
            assert self.value > self.left.value, f"Binary search violation: {self} has a left child of {self.left}"
            self.left.assert_sorted()
        if self.right is not None:
            assert self.value < self.right.value, f"Binary search violation: {self} has a right child of {self.right}"
            self.right.assert_sorted()
    
    def assert_avl(self):
        assert -1 <= self.balance_factor() <= 1, f"AVL violation: {self} reports a balance factor of {self.balance_factor()}"
        if self.left is not None:
            self.left.assert_avl()
        if self.right is not None:
            self.right.assert_avl()
    
    def assert_tree(self):
        if self.left is not None:
            assert self.left.parent is self, f"Tree violation: {self}'s left child is {self.left} but {self.left}'s parent is {self.left.parent}" 
            self.left.assert_tree()
        if self.right is not None:
            assert self.right.parent is self, f"Tree violation: {self}'s right child is {self.right} but {self.right}'s parent is {self.right.parent}"
            self.right.assert_tree()
    
    def size(self):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size()
        right_size = 0
        if self.right is not None:
            right_size = self.right.size()
        return left_size+right_size+1

if __name__ == "__main__":
    
    # Note that this IS NOT how you will actually build your trees.
    # This testing_tree is constructed by hand so that you can test
    # simpler methods before fully implementing the add and remove
    # functions.
    
    testing_tree = AVLTree()
    a_node = AVLTreeNode(None,4)
    testing_tree.root = a_node
    
    b_node = AVLTreeNode(a_node,2)
    a_node.left = b_node
    
    c_node = AVLTreeNode(a_node,6)
    a_node.right = c_node
    
    d_node = AVLTreeNode(b_node,1)
    b_node.left = d_node
    
    e_node = AVLTreeNode(b_node,3)
    b_node.right = e_node
    
    f_node = AVLTreeNode(c_node,5)
    c_node.left = f_node
    
    g_node = AVLTreeNode(c_node,7)
    c_node.right = g_node
    
    testing_tree.display()
