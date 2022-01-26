
import random

def mergesort(the_list,depth=0):

    print("\t"*depth,end="")
    print(f"{the_list} begins")
    
    # recursive case
    if len(the_list) > 1:

        # split list into two equal sublists
        # if list has odd # of elements, extra element goes right
        middle_index = len(the_list)//2
        left_list = the_list[:middle_index]
        right_list = the_list[middle_index:]

        # perform recursive sorts
        mergesort(left_list,depth+1)
        mergesort(right_list,depth+1)

        merged_index = 0
        left_index = 0
        right_index = 0

        # comparison loop
        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                # left is smaller
                the_list[merged_index] = left_list[left_index]
                left_index += 1
            else:
                # right is smaller (or they're equal)
                the_list[merged_index] = right_list[right_index]
                right_index += 1
            merged_index += 1

        # left dump
        while left_index < len(left_list):
            the_list[merged_index] = left_list[left_index]
            left_index += 1
            merged_index += 1

        # right dump
        while right_index < len(right_list):
            the_list[merged_index] = right_list[right_index]
            right_index += 1
            merged_index += 1

        

        
    # base case implicit - don't do anything
    print("\t"*depth,end="")
    print(f"{the_list} ends")
        
if __name__ == "__main__":
    my_list = list()
    for i in range(7):
        my_list.append(random.randint(0,10))
    print(f"Unsorted: {my_list}")
    mergesort(my_list)
    print(f"Sorted: {my_list}")
