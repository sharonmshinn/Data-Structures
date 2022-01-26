import os
import re
os.chdir("C:\\Users\\sharo\\OneDrive\\Documents\\CS Files")
from arraylist import ArrayList, SimpleArray



def main():

    TESTS = {'adjust index': test_adjust_index,
         'adjust array': test_adjust_internal_array,
         'append': test_append,
         'str': test_str,
         'extend': test_extend,
         'len': test_len,
         'getitem': test_getitem,
         'setitem': test_setitem,
         'contains': test_contains,
         'count': test_count,
         'index': test_index,
         'insert': test_insert,
         'remove': test_remove,
         'eq': test_eq
         }

    for test_name in TESTS:
        try:
            TESTS[test_name]()
            print(f"{test_name} tests passed")
        except AssertionError as e:
            print(e.args[0])

def test_adjust_index():
    test_list = ArrayList('a','b','c','d','e')
    assert test_list._adjust_index(4)==4, 'adjust index test 1 failed'
    try:
        test_list._adjust_index(5)
        assert False, 'adjust index test 2 failed'
    except IndexError:
        pass
    assert test_list._adjust_index(-1)==4, 'adjust index test 3 failed'
    assert test_list._adjust_index(-5)==0, 'adjust index test 4 failed'
    try:
        test_list._adjust_index(-6)
        assert False, 'adjust index test 5 failed'
    except IndexError:
        pass
    

def test_adjust_internal_array():
    test_list = ArrayList()
    test_list._adjust_internal_array(10)
    assert len(test_list.array)==10, 'adjust array test 1 failed'
    test_list._adjust_internal_array(11)
    assert len(test_list.array)==20, 'Adjust array test 2 failed'
    test_list._adjust_internal_array(161)
    assert len(test_list.array)==320, 'adjust array test 3 failed'
    test_list._adjust_internal_array(100)
    assert len(test_list.array)==160, 'adjust array test 4 failed'
    test_list._adjust_internal_array(8)
    assert len(test_list.array)==20, 'adjust array test 5 failed'
    test_list._adjust_internal_array(0)
    assert len(test_list.array)==10, 'adjust array test 6 failed'
    

def test_append():
    test_list = ArrayList(0,1,2,3,4,5,6,7,8)
    test_list.append(9)
    assert test_list.logical_size == 10, 'append test 1 failed'
    assert len(test_list.array)==10, 'append test 2 failed'
    assert test_list.array[9]==9, 'append test 3 failed'
    test_list.append(10)
    assert test_list.logical_size == 11, 'append test 4 failed'
    assert len(test_list.array)==20, 'append test 5 failed'
    assert test_list.array[10]==10, 'append test 6 failed'
    for i in range(10):
        test_list.append('more')
    assert test_list.logical_size == 21, 'append test 7 failed'
    assert len(test_list.array)==40, 'append test 8 failed'
    assert test_list.array[20] == 'more', 'append test 9 failed'

def test_str():
    test_list = ArrayList('a','b','c','d','e')
    assert re.fullmatch(r"\['a', ?'b', ?'c', ?'d', ?'e'\]",str(test_list)), 'str test 1 failed'
    test_list = ArrayList(0,1,2)
    assert re.fullmatch(r"\[0, ?1, ?2\]",str(test_list)), 'str test 2 failed'
    test_list = ArrayList()
    assert re.fullmatch(r"\[\]",str(test_list)), 'str test 3 failed'

def test_extend():
    test_list = ArrayList(0,1,2,3,4,5,6,7)
    test_list2 = ArrayList(8,9,10,11,12)
    test_list.extend(test_list2)
    assert test_list.logical_size == 13, 'extend test 1 failed'
    assert len(test_list.array) == 20, 'extend test 2 failed'
    assert test_list2.logical_size == 5, 'extend test 3 failed'
    assert len(test_list2.array) == 10, 'extend test 4 failed'
    assert test_list.array[8] == 8, 'extend test 5 failed'
    assert test_list.array[12] == 12, 'extend test 6 failed'
    test_list = ArrayList()
    test_list2 = ArrayList(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)
    test_list.extend(test_list2)
    assert test_list.logical_size == 22, 'extend test 7 failed'
    assert len(test_list.array) == 40, 'extend test 8 failed'
    assert test_list2.logical_size == 22, 'extend test 9 failed'
    assert len(test_list2.array) == 40, 'extend test 10 failed'
    assert test_list.array[0] == 0, 'extend test 11 failed'
    assert test_list.array[21] == 21, 'extend test 12 failed'

def test_len():
    test_list = ArrayList(0,1,2,3,4)
    assert len(test_list) == 5, 'len test 1 failed'
    test_list = ArrayList()
    assert len(test_list) == 0, 'len test 2 failed'

def test_getitem():
    test_list = ArrayList('a','b','c')
    assert test_list[0] == 'a', 'getitem test 1 failed'
    assert test_list[1] == 'b', 'getitem test 2 failed'
    assert test_list[2] == 'c', 'getitem test 3 failed'
    try:
        test_list[3] == 'd'
        assert False, 'getitem test 4 failed'
    except IndexError:
        pass
    assert test_list[-1] == 'c', 'getitem test 5 failed'
    assert test_list[-2] == 'b', 'getitem test 6 failed'
    assert test_list[-3] == 'a', 'getitem test 7 failed'
    try:
        test_list[-4] == 'z'
        assert False, 'getitem test 8 failed'
    except IndexError:
        pass

def test_setitem():
    test_list = ArrayList('a','b','c')
    test_list[0] = 'x'
    assert test_list.array[0] == 'x', 'setitem test 1 failed'
    test_list[1] = 'y'
    assert test_list.array[1] == 'y', 'setitem test 2 failed'
    test_list[2] = 'z'
    assert test_list.array[2] == 'z', 'setitem test 3 failed'
    try:
        test_list[3] = 'a'
        assert False, 'setitem test 4 failed'
    except IndexError:
        pass
    test_list[-1] = 'i'
    assert test_list.array[2] == 'i', 'setitem test 5 failed'
    test_list[-2] = 'j'
    assert test_list.array[1] == 'j', 'setitem test 6 failed'
    test_list[-3] = 'k'
    assert test_list.array[0] == 'k', 'setitem test 7 failed'
    try:
        test_list[-4] = 'bloop'
        assert False, 'setitem test 8 failed'
    except IndexError:
        pass

def test_contains():
    test_list = ArrayList('a','b','c','a','b','c','d')
    assert 'a' in test_list, 'contains test 1 failed'
    assert 'b' in test_list, 'contains test 2 failed'
    assert 'c' in test_list, 'contains test 3 failed'
    assert 'd' in test_list, 'contains test 4 failed'
    assert 'z' not in test_list, 'contains test 5 failed'
    assert None not in test_list, 'contains test 6 failed'
    assert '' not in test_list, 'contains test 7 failed'

def test_count():
    test_list = ArrayList('a','b','c','d','a','b','c','a','b','a')
    assert test_list.count('a')==4, 'count test 1 failed'
    assert test_list.count('b')==3, 'count test 2 failed'
    assert test_list.count('c')==2, 'count test 3 failed'
    assert test_list.count('d')==1, 'count test 4 failed'
    assert test_list.count('e')==0, 'count test 5 failed'
    assert test_list.count('')==0, 'count test 6 failed'
    assert test_list.count(None)==0, 'count test 7 failed'

def test_index():
    test_list = ArrayList('a','a','a','a','b','b','b','c','c','d')
    assert test_list.index('a') == 0, 'index test 1 failed'
    assert test_list.index('b') == 4, 'index test 2 failed'
    assert test_list.index('c') == 7, 'index test 3 failed'
    assert test_list.index('d') == 9, 'index test 4 failed'
    try:
        test_list.index('e')
        assert False, 'index test 5 failed'
    except ValueError:
        pass
    try:
        test_list.index(None)
        assert False, 'index test 6 failed'
    except ValueError:
        pass

def test_insert():
    test_list = ArrayList('a','b','c','d','e')
    test_list.insert(0,'newfirst')
    correct_vals = ('newfirst','a','b','c','d','e')
    for i in range(len(correct_vals)):
        assert test_list.array[i] == correct_vals[i], 'insert test 1 failed'
    assert test_list.logical_size == 6, 'insert test 2 failed'
    test_list = ArrayList('a','b','c','d','e','f','g','h','i','j')
    test_list.insert(5,'newmiddle')
    correct_vals = ('a','b','c','d','e','newmiddle','f','g','h','i','j')
    for i in range(len(correct_vals)):
        assert test_list.array[i] == correct_vals[i], 'insert test 3 failed'
    assert test_list.logical_size == 11, 'insert test 4 failed'
    assert len(test_list.array) == 20, 'insert test 5 failed'

def test_remove():
    test_list = ArrayList('a','b','c','d','e')
    returned_value = test_list.remove(0)
    assert returned_value == 'a', 'remove test 1 failed'
    correct_vals = ('b','c','d','e')
    for i in range(len(correct_vals)):
        assert test_list.array[i] == correct_vals[i], 'remove test 2 failed'
    assert test_list.logical_size == 4, 'remove test 3 failed'
    test_list = ArrayList('a','b','c','d','e')
    returned_value = test_list.remove(2)
    assert returned_value == 'c', 'remove test 4 failed'
    correct_vals = ('a','b','d','e')
    for i in range(len(correct_vals)):
        assert test_list.array[i] == correct_vals[i], 'remove test 5 failed'
    assert test_list.logical_size == 4, 'remove test 6 failed'
    test_list = ArrayList(0,1,2,3,4,5,6,7,8,9,10,11)
    for i in range(8):
        test_list.remove(0)
    assert len(test_list.array) == 10, 'remove test 7 failed'

def test_eq():
    test_list = ArrayList()
    assert test_list == test_list, 'eq test 1 failed'
    test_list = ArrayList('a','b','c')
    assert test_list == ArrayList('a','b','c'), 'eq test 2 failed'
    assert test_list != ArrayList('a','b','c','d'), 'eq test 3 failed'
    assert test_list != ArrayList('a','b'), 'eq test 4 failed'
    assert test_list != ['a','b','c'], 'eq test 5 failed'
    assert test_list != ('a','b','c'), 'eq test 6 failed'
    
    test_list = ArrayList()
    test_list.array = SimpleArray(10)
    for i in range(10):
        test_list.array[i] = 50+i
    test_list.logical_size = 9
    test_list2 = ArrayList()
    test_list2.array = SimpleArray(20)
    for i in range(20):
        test_list2.array[i] = 50+i
    test_list2.logical_size = 9
    assert test_list == test_list2, 'eq test 7 failed'

if __name__ == "__main__":
    main()
