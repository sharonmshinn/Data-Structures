
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
            AVLTree.root = self.root.add(value)


    
    def remove(self,value):
        if self.root is not None:
            print(f"{self.root}")
            AVLTree.root = self.root.remove(value)
        else:
            return None
    
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
            print(f"{self.value} is equal to {value}. Value found!")
            return True
        elif value > self.value and self.right is not None:
            print(f"{self.value} compared to {value}")
            self.right.lookup(value)
        elif value < self.value and self.left is not None:
            self.left.lookup(value)
            print(f"{self.value} compared to {value}")
        elif self.left is None and self.right is None:
            print(f"{value} not found")
            return False

                
    
    def root(self):
        if self.root is None:
            return None
        elif self.parent is None:
            return self.root
        else:
            return self.parent.root()

    
    def add(self,value):
        if self.root is None:
            self.root = AVLTreeNode(None, value)
        elif value > self.value and self.right is not None:
            print(f"{value} bigger than {self.value}")
            print(f"node{self} with P:{self.parent}")
            
            self.right.add(value)
        elif value < self.value and self.left is not None:
            print(f"{value} smaller than {self.value}")
            print(f"node{self} with P:{self.parent}")
            
            self.left.add(value)
        elif value > self.value and self.right is None:
            print(f"{value} bigger than {self.value} and found spot")
            print(f"node{self} with P:{self.parent}")
            print(f"{self.root}")
            
            self.right = AVLTreeNode(self.value, value)
        elif value < self.value and self.left is None:
            print(f"{value} bigger than {self.value} and found spot")
            print(f"node{self} with P:{self.parent}")
            print(f"{self.root}")
            
            self.left = AVLTreeNode(self.value, value)
        elif value == self.value:
            print(f"{value} the same as {self.value}. Already in tree")
            print(f"node{self} with P:{self.parent}")
            print(f"{self.root}")
            
            return
        return self.root()
            
    
    def rightmost_descendent(self):
        if self.right is None:
            return self 
        else:
            return self.right.rightmost_descendent()

    
    def notify_parent(self,new):
        print(f"Us: {self} Parent:{self.parent}")
        if self is self.parent.left:
            self.left = new
        elif self is self.parent.right:
            self.right = new
    
    def remove(self,value):
        if self.value < value and self.right is not None:
            print(f"{value} bigger than {self.value}")
            self.right.remove(value)
        elif self.value > value and self.left is not None:
            print(f"{value} smaller than {self.value}")
            self.left.remove(value)
        elif self.value < value and self.right is None:
            print(f"{value} bigger than {self.value} and no options left")
            return self.root
        elif self.value > value and self.left is None:
            print(f"{value} smaller than {self.value} and no options left")
            return self.root
        elif self.value == value:
            print(f"{value} same as {self.value}")
            print(f"{self} looking for children")
            print(f"{self}'s children are R: {self.right} and L: {self.left} and P: {self.parent}")

            #if tree only has a root
            if self.parent is None and self.value == value:
                if self.left is None and self.right is None:
                    self.value = None
                elif self.left is not None and self.right is None:
                    self.value = self.left
                elif self.left is None and self.right is not None:
                    self.value = self.right
                elif self.left is not None and self.right is not None:
                #if root has children
                #right rotation
                    pass
            
            #no child case
            elif self.left is None and self.right is None:
                print(f"{self} has no children and P:{self.parent}")
                self = self.notify_parent(AVLTreeNode(self.parent,None))
                return self.root
            #one-child case
            #left-child case
            elif self.right is None and self.left is not None:
                print(f"{self} has one child, L:{self.left}")
                
                
                

            #two-child case
            
        #return self.root
    
    def height(self):
        if self.left and self.right is not None:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left is not None:
            return 1 + self.left.height()
        elif self.right is not None:
            return 1 + self.right.height()
        else:
            return 1
            
        
        #other way

    
    def balance_factor(self):
        if self.right and self.left is None:
            return 0
        else:
            return self.right.height() - self.left.height()
            
            

    # not sure how to approach
    #is this recursive?
    #balance factor is total height of left subtree vs right subtree?
    #or leftmost and rightmost height
            
            
        
    
    def rotate_right(self):
        y = self.left
        self.left = y.right
        if y.right is not None:
            y.right.parent = self
        y.parent = self.parent
        if self.parent is None:
            self.root = y
        elif self == self.parent.right:
            self.parent.right = y
        else:
            self.parent.left = y
        
            
    
    def rotate_left(self):
        pass
        #TODO: Implement method
    
    def check_up(self):
        pass
        #TODO: Implement method
    
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
