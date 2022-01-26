
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

            return_root = self.parent
            print(f"{value} same as {self.value}")
            print(f"{self} looking for children")
            print(f"{self}'s children are R: {self.right} and L: {self.left} and P: {self.parent}")
            
            #no child case
            if self.left is None and self.right is None:
                print(f"{self} has no children")
                if self.parent is None:
                    print(f"{self} has no children or parent and is the root")
                    return None
                else:
                    print(f"return_root is {return_root}")
                    print(f"{self} has no children, but has P:{self.parent}")
                    self = self.parent 
                    


            #one-child case
            #left-child case
            elif self.right is None and self.left is not None:
                if self.parent is None:
                    print(f"{self} with left child {self.left}")
                    self.value = self.left.value
                    self.left = None
                    print(f"{self}")
                    return self.root()
                else:
                    self = self.notify_parent(self.left)
                    return return_root.root()
                    
                    

                    
            #right-child-case
            elif self.right is not None and self.left is None:
                if self.parent is None:
                    print(f"{self} with right child{self.right}")
                    self.value = self.right.value
                    self.right = Non                    print(f"{self}")
                    return self.root()
                else:
                    self = self.notify_parent(self.right)
                    return return_root.root()
                    


            #two-child case
            elif self.right is not None and self.left is not None:
                if self.parent is None:
                    print(f"{self} has children L:{self.left} and R:{self.right}")
                    print(f"{self} is the root:{self.root}")
                    new_root = self.left.rightmost_descendent()
                    print(f"{new_root} switching with {self}")
                    temp = self.value
                    self.value = new_root.value
                    new_root.value = temp
                    
                    print(f"Values swapped. Now removing {new_root.value}")
                    if new_root.left is not None:
                        self.left.right = new_root.left
                    else:
                        self.left.right = None
                else:
                    pass
    
                                                
                return self.root()
                
                
                

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

        old_root = self
        print(f"{self} is self")
        print(f"Self's parent is {self.parent}")
        self.parent = old_root.left
        self.parent.left = old_root.left.left
        if old_root.left.right is not None:
            kidnap_node = self.left.right
            print(f"kidnapped node is {kidnap_node}")
            self.left.right = None
            self.left = kidnap_node
            
                    old_root = self
        print(f"{self} is self")
        if self.left.right is not None:
            kidnap_node = self.left.right
            print(f"kidnapped node is {kidnap_node}")
            self.left.right = None
        print(f"Self's parent is {self.parent}")
        self.parent = self.left
        self.parent.left = self.left.left
        self.left = kidnap_node
        
        
        print(f"{self}'s parent is now {self.parent}")





                new_right = self
        print(f"{new_right}")
        new_root = self.left
        print(f"{new_root}")
        new_left = self.left.left
        print(f"{new_left}")
        print(f"{new_root.parent}")
        new_root.parent = None
        print(f"{new_root.parent}")
        new_right.left = None
        print(f"{new_right.left}")
        if new_right.parent is None:
            print(f"{self} is now {new_root}")
            self = new_root
            print(f"See? {self}. with children R:{self.right} and L:{self.left}")
            if new_root.right is not None:
                kidnap_value = new_root.right
                new_root.right = None
                print(f"{new_root} right value is now {new_root.right}")
                print(f"kidnap_value is {kidnap_value}")
            self.root = new_root
            print(f"{self}")
        
            
    
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
    
