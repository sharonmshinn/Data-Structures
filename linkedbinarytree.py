
class BinaryTree:

    def __init__(self):
        self.root = None

    def __len__(self):
        if self.root:
            return len(self.root)
        else:
            return 0

    def display(self):
        if self.root:
            self.root.display_subtree("X")
    

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

class BinarySearchTree(BinaryTree):

    def add(self,value):

        new_node = TreeNode(value)
        
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                elif value > current_node.value:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
                else:
                    break

    def search(self,value):
        current_node = self.root

        while True:
            if current_node is None:
                return False
            elif value == current_node.value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def remove(self,value):

        if self.root is None:
            return False

        # deleting root?
        if self.root.value == value:

            # no child root
            if self.root.left is None and self.root.right is None:
                self.root = None
            # left child only root
            elif self.root.right is None:
                self.root = self.root.left
            # right child only root
            elif self.root.left is None:
                self.root = self.root.right
            # two children :( :( :(
            else:
                rightmost_descendent = self.root.left
                while rightmost_descendent.right is not None:
                    rightmost_descendent = rightmost_descendent.right
                kidnap_value = rightmost_descendent.value
                self.remove(kidnap_value)
                self.root.value = kidnap_value
            
        else:
            current_node = self.root
            which_child = ""

            while True:
                # check left
                if value < current_node.value:
                    if current_node.left is None:
                        return
                    elif value == current_node.left.value:
                        which_child = "left"
                        break
                    else:
                        current_node = current_node.left
                # check right
                elif value > current_node.value:
                    if current_node.right is None:
                        return
                    elif value == current_node.right.value:
                        which_child = "right"
                        break
                    else:
                        current_node = current_node.right

            if which_child == "left":
                node_to_delete = current_node.left
            else:
                node_to_delete = current_node.right
            # no children
            if node_to_delete.left is None \
               and node_to_delete.right is None:
                if which_child == "left":
                    current_node.left = None
                else:
                    current_node.right = None
            # left child only
            elif node_to_delete.right is None:
                if which_child == "left":
                    current_node.left = node_to_delete.left
                else:
                    current_node.right = node_to_delete.left
            # right child only
            elif node_to_delete.left is None:
                if which_child == "left":
                    current_node.left = node_to_delete.right
                else:
                    current_node.right = node_to_delete.right
            # two children :( :( :(
            else:
                rightmost_descendent = node_to_delete.left
                while rightmost_descendent.right is not None:
                    rightmost_descendent = rightmost_descendent.right
                kidnap_value = rightmost_descendent.value
                self.remove(kidnap_value)
                node_to_delete.value = kidnap_value
            
        
                
    

if __name__ == "__main__":
    my_tree = BinarySearchTree()
    my_tree.add(5)
    my_tree.add(7)
    my_tree.add(3)
    my_tree.add(1)
    my_tree.add(19)
    my_tree.add(23)
    my_tree.add(6)
    my_tree.add(6)
    my_tree.add(4)
    my_tree.add(50)
    my_tree.display()
    my_tree.remove(5)
    my_tree.display()
    #print(my_tree.search(19))
    #print(my_tree.search(8))
    #print(my_tree.search(50))
    #print(my_tree.search(99))
