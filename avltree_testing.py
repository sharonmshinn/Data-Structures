import os
os.chdir("C:\\Users\\sharo\\OneDrive\\Documents\\CS Files\\CS 1107")
from avltree import AVLTree
import random
import logging
logging.basicConfig(level=logging.DEBUG)

def test_random_tree(seed=7355608,n=100,min_val=1,max_val=100):
    test_tree = AVLTree()
    random.seed(seed)
    nodes_to_add = list()
    for i in range(n):
        nodes_to_add.append(random.randint(min_val,max_val))
    nodes_to_remove = nodes_to_add[:] # make a copy of the list...
    random.shuffle(nodes_to_remove) # ...and shuffle it
    
    values_present = set()
    all_values = set(range(min_val,max_val+1))
    
    check_all_validity(test_tree,all_values,values_present)
    
    for value in nodes_to_add:
        logging.info(f"Adding {value}")
        old_size = len(test_tree)
        logging.info(f"Current size {old_size}")
        if value in values_present:
            expected_size = old_size
        else:
            expected_size = old_size + 1
        test_tree.add(value)
        values_present.add(value)
        new_size = len(test_tree)
        assert expected_size == new_size, f"Expected size {expected_size} after adding {value}, actual size {new_size}"
        check_all_validity(test_tree,all_values,values_present)
    
    for value in nodes_to_remove:
        logging.info(f"Removing {value}")
        old_size = len(test_tree)
        logging.info(f"Current size {old_size}")
        if value in values_present:
            expected_size = old_size - 1
        else:
            expected_size = old_size
        test_tree.remove(value)
        values_present -= {value}
        new_size = len(test_tree)
        assert expected_size == new_size, f"Expected size {expected_size} after removing {value}, actual size {new_size}"
        check_all_validity(test_tree,all_values,values_present)
    logging.info("CONGLATURATION MISSION SUCCESS")

def check_all_validity(tree,all_values,values_present):
    tree.assert_valid()
    check_all_present(tree,values_present)
    check_all_absent(tree,all_values-values_present)

def check_all_present(tree,values):
    for val in values:
        assert tree.lookup(val)

def check_all_absent(tree,values):
    for val in values:
        assert not tree.lookup(val)
    
if __name__ == "__main__":
    test_random_tree()
