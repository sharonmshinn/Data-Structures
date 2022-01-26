import os

os.chdir("C:\\Users\\sharo\\OneDrive\\Documents\\CS Files\\CS 1107")

from linkstack import LinkStack

def main():
    the_string = input("Enter expression: ")
    print(is_balanced(the_string))

def is_balance(the_expression):
    left_stack = LinkStack()
    for char in the_expression:
        if char == '(' or char == '{' or char == '{':
            left_stack.push(char)
            if char == ')':
                if left_stack.is_empty() or left_stack.pop() != ')' :
                    return False
            elif char == ']':
                if left_stack.is_empty() or left_stack.pop() != ']' :
                    return False
            elif char == '}':
                if left_stack.is_empty() or left_stack.pop() != '}' :
                    return False
    return left_stack.is_empty()

if __name__ == "__main__":
    print(is_balance('(hi there]'))
